# 环境搭载
## ubuntu
```
https://blog.csdn.net/FSKEps/article/details/118493578
```
## g++
```
https://blog.csdn.net/ggggyj/article/details/117691948
```
```
update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.8 100

update-alternatives --config gcc
```
## mobaxterm（SSH）
```
https://blog.csdn.net/qq_44074697/article/details/118544904
```
## docker
```
docker run -d -it --name xxx -v /data/zhangrun:/root 58db3edaf2be 
```

‘58db3edaf2be’为ubuntu镜像id，地址提供映射

```
docker exec -it xxx bash
```
## gem5
```
https://zhuanlan.zhihu.com/p/336017753
```

```
git clone https://github.com/gem5/gem5.git
```

```
sudo apt install build-essential git m4 scons zlib1g zlib1g-dev libprotobuf-dev protobuf-compiler libprotoc-dev libgoogle-perftools-dev python3-dev python-is-python3 libboost-all-dev pkg-config
```

```
cd gem5
```

```
scons build/X86/gem5.opt -j 8
scons build/ARM/gem5.fast -j56
```

```
aarch64-linux-gnu-g++ mytest.c -static -o mytest
./build/ARM/gem5.fast ./configs/example/se.py  -c ./mytest
```
## git
```
https://blog.csdn.net/m0_37592397/article/details/78664757
https://zhuanlan.zhihu.com/p/136355306

设置安全目录
git config --global --add safe.directory /root/.ssh
```
## aarch64-linux-gcc
```
https://blog.csdn.net/baidu_41191295/article/details/116533066
```

```
https://linux-packages.com/linux-mint-20-3/package/gfortran-aarch64-linux-gnu
```
## qemu
```
https://zhuanlan.zhihu.com/p/345232459
```
## spec
spec2006：
```
https://pacman.cs.tsinghua.edu.cn/~whj/pubs/cpu2006-1.2.iso
```
spec2017：
```
https://pacman.cs.tsinghua.edu.cn/~whj/pubs/cpu2017-1.0.2.iso
```

# 知识框架
## gem5（CPU系统）
* 假如现在有一个场景，要测试cache大小对cpu性能的影响，直接硬件测试是十分困难的，每次都给硬件换一块cache吗？显然不现实的。  那么此时就需要一个软件的模拟器，可以用一个程序来模拟一块cpu的执行过程，每次只改cache相关参数，重新运行程序即可。
* gem5是一个可以提供丰富硬件模拟功能的【软件模拟器】。
* 在进行体系结构research、design、benchmarking、profiling中，一个优秀的软件模拟器可以提供简单易实现的（相对而言）硬件设计以及快速性能评估。
## spec
* Benchmark就像高考一样，他的中文名是基准测试，是评价CPU性能的一个标尺。不同的benchmark就像不同的科目，考量CPU的不同方面。为了尽可能的全面，有些benchmark是成套发布的，里面有好几种不同的benchmarks。
* 学术界用的最多的还是SPEC公司的benchmark，benchmark的名字也叫做SPEC。它包含了经典astar、bzip2、gcc、perlbench等测试程序，以C语言为主。
## gem5跑spec
* 要设计一个新的cpu微架构，这个架构跑spec很快。 那么首先得看现在cpu跑spec有什么瓶颈，在哪里卡住了？ 哪个部件需要改进？ 所以要跑起来统计一些微架构信息，再通过gem5改进这个部件。
## profiling与性能优化
```
https://zhuanlan.zhihu.com/p/362575905
```
## blockisa
* 自制模拟的cpu系统，后期通过gem5跑spec来测试性能，最后以针对性的优化该系统。
```
./build/ARM/gem5.opt --debug-flags=BCU,BEU,fetch1,execute,Fetch,Drain,Cache,BEUExecute,Decode,Branch,BEUMem ./configs-mc.py > out.txt
```
## checkpoint
* 在做体系结构研究的时候,常用 GEM5 作为仿真器, GEM5 有个优点就是仿真很准,当然,作为代价就是太慢太慢太慢了. 电脑上1s跑完的程序 GEM5 能给你跑十几个小时,常规的小的 benchmark 跑一天两天是常态.
* 在这种情况下, Simpoint 登场了. Simpoint 的思想很简单,注意到不管多复杂的一个程序,它在绝大多数时间做的执行的操作就那么几个,如果我们能统计出那几个主要的操作以及它们所占的比例,是不是只对那几个操作做仿真再加权就可以了.
* 以 Simpoint 的思想为指导,我们对在 GEM5 里面做加速建立了一个大体的框架:<br>
    1)使用 Simpoint ,得到程序分成的片段以及其权重 <br>
    2)根据片段生成 checkpoint <br>
    3)每次再运行程序的时候只需要重载 checkpoint 

# 代码尝试
- tmux
```
创建 tmux
在里面进入docker 运行程序
退出 Ctrl + B -> D
结束 Ctrl + D
```

my search：
```
学峰文档
https://docs.cd speqq.com/doc/DYlhLa1FHeW5JRUhL
```
```
gem5运行spec2017
https://zhuanlan.zhihu.com/p/222595617

gem5运行spec2006
https://blog.csdn.net/fandroid/article/details/45701463

spec2017运行指南
https://www.spec.org/cpu2017/Docs/install-guide-unix.html#test

spec排bug
https://blog.csdn.net/Z_july/article/details/108001228

gem5 run spec2017 detail
https://zhuanlan.zhihu.com/p/607111813

gem5 checkpoint
https://blog.csdn.net/wyj7260/article/details/44340079

https://blog.csdn.net/JaCenz/article/details/129851521

https://zhuanlan.zhihu.com/p/453370789

https://github.com/lshpku/gem5-fs-handbook/blob/master/gem5_Checkpoint.md

simpoint在gem5仿真加速
https://zhuanlan.zhihu.com/p/453370789
```

- 先验尝试

spec2017
```
source shrc
ulimit -s unlimited

runcpu --config=spec2017_X86 --reportable intrate intspeed fprate fpspeed
```

g++/aarch64 build a test and gem5 run
```
vi mytest.c
g++ mytest.c -o mytest
./build/X86/gem5.fast ./configs/example/se.py --cpu-type=NonCachingSimpleCPU --mem-size=16GB --mem-type=SimpleMemory  -c ./mytest

scons build/ARM/gem5.opt -j64
aarch64-linux-gnu-g++ mytest.c -static -o mytest
./build/ARM/gem5.fast ./configs/example/se.py --cpu-type=NonCachingSimpleCPU --mem-size=16GB --mem-type=SimpleMemory  -c ./mytest
```

gem5 run spec2017
```
./run_spec17.sh perlbench_s /root/gem5/m5out
```

- 杂七杂八
``` 
/vim/
ctrl+v up/down shift+i # esc
ctrl+v up/down d

/XXX n
:noh  取消上次搜索的高亮结果

:sp address
:vs/vsp address
ctrl w w

:n1,n2s/s1/s2/gc
    g：globe,表示全局替换
    c：confirm,表示进行确认
    p：表示替代结果逐行显示(Ctrl + L恢复屏幕)
    i：ignore,不区分大小写
    "1,n"：表示从第1行到n行
    "%"：表示整个文件,同"1,$"
    ".,$"：表示从当前行到文件尾
    s1和s2中的特殊字符需要使用转义符号\,进行转义

/decompress/
tar –xvf file.tar  解压 tar包
tar -xzvf file.tar.gz 解压tar.gz
tar -xjvf file.tar.bz2   解压 tar.bz2
tar –xZvf file.tar.Z   解压tar.Z
unrar e file.rar 解压rar
unzip file.zip 解压zip

/grade change/
update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.9 100
update-alternatives --config gcc

/tmux/
tmux new -s <session-name>
tmux detach
tmux ls
tmux attach -t <session-name>
tmux kill-session -t <session-name>
tmux switch -t <session-name>
tmux rename-session -t <old-name> <new-name>

Ctrl+b d：分离当前会话
Ctrl+b s：列出所有会话
Ctrl+b $：重命名当前会话
```

- bug

[![p9EH35D.png](https://s1.ax1x.com/2023/04/21/p9EH35D.png)](https://imgse.com/i/p9EH35D)

525 simpoint--1
[![p906YLt.png](https://s1.ax1x.com/2023/05/09/p906YLt.png)](https://imgse.com/i/p906YLt)

mytest simpoint--1
[![p9BJQER.png](https://s1.ax1x.com/2023/05/09/p9BJQER.png)](https://imgse.com/i/p9BJQER)

mytest simpoint--3
[![p9BJlU1.png](https://s1.ax1x.com/2023/05/09/p9BJlU1.png)](https://imgse.com/i/p9BJlU1)

mytest simpoint--4
[![p9gWDJJ.png](https://s1.ax1x.com/2023/05/15/p9gWDJJ.png)](https://imgse.com/i/p9gWDJJ)

---
bug --> test checkpoint from website

build/X86/gem5.debug --outdir=/root/gem5/m5out/spec2017/spec2017_checkpoint configs/example/se.py --take-simpoint-checkpoint=/root/SimPoint.3.2/output/gem5/spec2017/spec2017_simpoint_file,10000000,1000000 --cpu-type=AtomicSimpleCPU --caches --l2cache --l1i_size 64kB --l1d_size 32kB --l2_size 1MB --l1i_assoc 8 --l1d_assoc 8 --l2_assoc 16 --cacheline_size 128 --mem-type DDR3_2133_8x8 --mem-size 16GB --l2-hwp-type StridePrefetcher -c /root/gem5/configs/spec2017/525.x264_r -o ' -s 13 -e 12'

./build/X86/gem5.debug --outdir=m5out/spec2017/spec2017_init ./configs/example/se.py --simpoint-profile --simpoint-interval 10000000 --cpu-type=NonCachingSimpleCPU -c /root/gem5/configs/spec2017/525.x264_r/imagevalidate_525_base.mytest-64 -o ' -s 13 -e 12'

---
- checkpoint --> zxf

1:生成simpoint

2:生成关键点

3:打checkpoint

4:跑出所有checkpoint数据

---
source ./xxx.sh = . ./xxx.sh != ./xxx.sh

source在当前bash环境下执行命令，而scripts是启动一个子shell来执行命令。

如果把设置环境变量的命令写进scripts中，就只会影响shell,无法改变当前的bash,所以通过命令列设置环境变量时，要用source 命令。

e.g.
```
# cat test.sh 
#! /bin/bash
test=1234

# ./test.sh 
# echo $test

# . ./test.sh
# echo $test
1234

# source ./test.sh
echo $test
123
```

bash ./xxx.sh = sh ./xxx.sh != source ./xxx.sh

前者是重新启动一个subshell，在subshell中执行脚本，脚本设置的变量在执行结束不会保留。后者是在当前shell中执行脚本，脚本中设置的变量在执行结束后会保留。

（但如果前者运行的脚本不以#!bin/bash开头，那也不会在subshell中运行）

"#!/bin/sh"是对shell的声明，说明你所用的是那种类型的shell及其路径所在。

#! /bin/sh 是指此脚本使用/bin/sh来解释执行，#!是特殊的表示符，其后面跟的是解释此脚本的shell的路径
```
/root/gem5/configs/spec2017/se_mytest.py
/root/gem5-dsim3
--ds-config /root/gem5-dsim3/ext/dramsim3/DRAMsim3/configs/DDR4_8Gb_x16_3200.ini
```

- new task
```
note:simTicks, mem_ctrl.*total
two tables:regard ds-config as different types
run:all the spec benchmarks
```
