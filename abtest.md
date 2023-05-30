# A/B TEST
A/B TEST的目的是收集数据，作出决定。在置信区间内计算效能，为了判断我们的结果有多大可能具有可重复性与合理性，并做出正确的决定。

## When can you use A/B testing：
- 对照组和实验组（是否容易设置两组）
- 明确的归因（归因是否清晰？）
- 排除其他影响（设备？人群？）
- 时间成本（回馈是否过长？）

## Other methods you can use：

- Customer funnel

- click-through-rate and click-through-probability

- if N * p_hat > 5, then you can assume it is normal.
you should also check N * (1 - p_hat) > 5 satisfied.

## 合并标准误差：
- 合并概率：p_hat = (x1 + x2) / (n1 + n2)
- 合并标准误差：se = sqrt(p_hat * (1 - p_hat) * (1 / n1 + 1 / n2))
- 预计差异：d_hat = x1/n1 - x2/n2
- 误差幅度：m = se * 置信水平对应上分位数（双侧）
- 置信水平下限：d_hat - m（上限同理），需要大于d_min实际显著性

## 实际显著性（是否看到你感兴趣的改变）
- 显著性差异：不同领域标准不同
- 统计显著性（假设检验） - 可重复性
- 统计显著性低于实际显著性

## 统计功效和规模
- AB两组真的存在差异时，能正确判断的概率
- 二者呈负向
- 确保功效，得到高概率结果 -> 具有统计显著性

## P值
- 原假设成立时，出现当前情况的概率
- p值越小，越容易拒绝原假设

## Tuskegee梅毒实验
该农村男性接受政府免费治疗--被用于研究非治疗下梅毒的自然发展过程

