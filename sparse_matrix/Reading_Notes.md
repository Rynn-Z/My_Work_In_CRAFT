# **稀疏矩阵**
## **WACO**
### 摘要
- 利用稀疏卷积网络学习稀疏图案的特征，使用专门设计的调度模板在格式和调度中嵌入耦合行为
- 新的搜索策略：近似最近邻搜索 -> 有效地、准确地检索给定稀疏模式的最佳格式和调度

### 介绍
- 与在密集张量代数中不同，只要考虑张量的形状，稀疏张量代数的性能很大程度上依赖于张量复杂的稀疏模式
- TACO：稀疏张量代数编译器 -> 通过引入一个格式抽象，概括了许多提议的稀疏格式
- 稀疏迭代空间变换框架：允许编译器生成具有调度的代码，该调度执行循环分割、重新排序、并行化和其他任务 -> 以探索迭代空间的不同遍历顺序
- <u>已经建立了编译器的机制，使代码生成支持许多不同的格式和调度，编译器为给定的稀疏性模式决定最佳格式和最佳调度的策略尚未设计</u>
- 设计此策略与程序的自动调优问题密切相关，单一的格式和固定的实现不能对所有的稀疏模式做到全局优化
- 程序自动调优 -> 优化稠密张量程序 -> <u>性能取决于输入的大小</u> -> 通过对给定的输入形状进行经验性的程序转换
- Halide, Tiramisu,and TVM -> 将算法与调度基元解耦，以转变稠密张量程序中的循环结构 -> 允许表达更广泛的算法 and 因为调度而引入了一个巨大的搜索空间
- 目前的生产和最先进的研究系统有以下局限性
1. 捕获稀疏模式的局限性：
    现有的方法要么依赖人为制作的特征要么依赖降采样矩阵的卷积神经网络
2. 缺乏协同优化：
    考虑格式和调度之间的耦合行为
3. 本文方法：提出一个框架，对给定的稀疏模式，自动且联合优化格式和调度 -> 基于成本模型的深度学习 -> 新的稀疏卷积网络 -> 统一的调度模板-快速调度 -> 使用近似最近邻搜索 -> 快速搜索最佳的格式和调度

### 概述
<div align=center><img width = '400' height ='600' src ="https://s1.ax1x.com/2023/06/29/pCwHMM4.png"/></div>

- 设计成本模型预测程序运行时间，成本模型使用稀疏矩阵和超级调度，统一的模板同时定义格式和调度（1-a）
- 训练成本模型后，建立KNN图 -> 建立在均匀采样的超级调度的程序嵌入上（1-b）
- 对于一个给定的稀疏矩阵输入①，ANNS重复②、③两步，直至它收敛到一个局部最优的超级调度（1-c）

### 动机举例
<div align=center><img width = '400' height ='400' src ="https://s1.ax1x.com/2023/06/29/pCwOm79.png"/></div>

1. 协同优化的影响
- Table1通过比较三个不同调优空间上的自动调优结果：格式、调度 -> 显示了稀疏张量程序中协同优化的影响（其中基线使用有TACO生成的CSR调度）

2. 稀疏性模式依赖的性质
- 稀疏张量程序的性能对输入矩阵的稀疏性模式非常敏感，没有任何一种格式或实现可以显示所有稀疏模式的最佳性能，Table2可证实上述性质

### 回顾