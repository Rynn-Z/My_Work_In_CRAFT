# Copyright (c) 2012-2013 ARM Limited
# All rights reserved.
#
# The license below extends only to copyright in the software and shall
# not be construed as granting a license to any other intellectual
# property including but not limited to intellectual property relating
# to a hardware implementation of the functionality of the software
# licensed hereunder.  You may use the software subject to the license
# terms below provided that you ensure that this notice is replicated
# unmodified and in its entirety in all distributions of the software,
# modified or unmodified, in source code or in binary form.
#
# Copyright (c) 2006-2008 The Regents of The University of Michigan
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met: redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer;
# redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution;
# neither the name of the copyright holders nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# Simple test script
#
# "m5 test.py"

import pdb

import argparse
import sys
import os

import m5
from m5.defines import buildEnv
from m5.objects import *
from m5.params import NULL
from m5.util import addToPath, fatal, warn
from gem5.isas import ISA
from gem5.runtime import get_runtime_isa

addToPath("../")

from ruby import Ruby

from common import Options
from common import Simulation
from common import CacheConfig
from common import CpuConfig
from common import ObjectList
from common import MemConfig
from common.FileSystemConfig import config_filesystem
from common.Caches import *
from common.cpu2000 import *
import spec17_benchmarks 

def get_processes(args):
    """Interprets provided args and returns a list of processes"""

    multiprocesses = []
    inputs = []
    outputs = []
    errouts = []
    pargs = []

    # pdb.set_trace()
    workloads = args.cmd.split(";")
    if args.input != "":
        inputs = args.input.split(";")
    if args.output != "":
        outputs = args.output.split(";")
    if args.errout != "":
        errouts = args.errout.split(";")
    if args.options != "":
        pargs = args.options.split(";")

    idx = 0
    for wrkld in workloads:
        process = Process(pid=100 + idx)
        process.executable = wrkld
        process.cwd = os.getcwd()
        process.gid = os.getgid()

        if args.env:
            with open(args.env, "r") as f:
                process.env = [line.rstrip() for line in f]

        if len(pargs) > idx:
            process.cmd = [wrkld] + pargs[idx].split()
        else:
            process.cmd = [wrkld]

        if len(inputs) > idx:
            process.input = inputs[idx]
        if len(outputs) > idx:
            process.output = outputs[idx]
        if len(errouts) > idx:
            process.errout = errouts[idx]

        multiprocesses.append(process)
        idx += 1

    if args.smt:
        # assert args.cpu_type == "DerivO3CPU"
        return multiprocesses, idx
    else:
        return multiprocesses, 1


parser = argparse.ArgumentParser()
Options.addCommonOptions(parser)
Options.addSEOptions(parser)
parser.add_argument("--benchmark", type=str, default="", help="The SPEC benchmark to be loaded.")
parser.add_argument("--benchmark_stdout", type=str, default="", help="Absolute path for stdout redirection for the benchmark.")
parser.add_argument("--benchmark_stderr", type=str, default="", help="Absolute path for stderr redirection for the benchmark.")


parser.add_argument(
    "--ds-config",
    default="/root/gem5-dsim3/ext/dramsim3/DRAMsim3/configs/DDR4_8Gb_x16_2133.ini",
    help="dramsim3 config file",
)

if "--ruby" in sys.argv:
    Ruby.define_options(parser)

args = parser.parse_args()

multiprocesses = []
numThreads = 1

if args.benchmark:
    print('Selected SPEC_CPU2017 benchmark')
    benches = args.benchmark.split(",")
    for i in range(len(benches)):
        if benches[i] == '500.perlbench_r':
            print('--> 500.perlbench_r')
            multiprocesses.append(spec17_benchmarks.perlbench_r)
        elif benches[i] == '502.gcc_r':
            print('--> gcc_r')
            multiprocesses.append(spec17_benchmarks.gcc_r)
        elif benches[i] == '505.mcf_r':
            print('--> 505.mcf_r')
            multiprocesses.append(spec17_benchmarks.mcf_r)
        elif benches[i] == '520.omnetpp_r':
            print('--> 520.omnetpp_r')
            multiprocesses.append(spec17_benchmarks.omnetpp_r)
        elif benches[i] == '523.xalancbmk_r':
            print('--> 523.xalancbmk_r')
            multiprocesses.append(spec17_benchmarks.xalancbmk_r)
        elif benches[i] == '525.x264_r':
            print('--> 525.x264_r')
            multiprocesses.append(spec17_benchmarks.x264_r)
        elif benches[i] == '531.deepsjeng_r':
            print('--> 531.deepsjeng_r')
            multiprocesses.append(spec17_benchmarks.deepsjeng_r)
        elif benches[i] == '541.leela_r':
            print('--> 541.leela_r')
            multiprocesses.append(spec17_benchmarks.leela_r)
        elif benches[i] == '548.exchange2_r':
            print('--> exchange2_r')
            multiprocesses.append(spec17_benchmarks.exchange2_r)
        elif benches[i] == '557.xz_r':
            print('--> 557.xz_r')
            multiprocesses.append(spec17_benchmarks.xz_r)
        elif benches[i] == '999.specrand_ir':
            print('--> 999.specrand_ir')
            multiprocesses.append(spec17_benchmarks.specrand_ir)
        elif benches[i] == '400.perlbench':
            print('--> 400.perlbench')
            multiprocesses.append(spec06_benchmarks.perlbench)
        elif benches[i] == '401.bzip2':
            print('--> 401.bzip2')
            multiprocesses.append(spec06_benchmarks.bzip2)
        elif benches[i] == '403.gcc':
            print('--> 403.gcc')
            multiprocesses.append(spec06_benchmarks.gcc)
        elif benches[i] == '429.mcf':
            print('--> 429.mcf')
            multiprocesses.append(spec06_benchmarks.mcf)
        elif benches[i] == '445.gobmk':
            print('--> 445.gobmk')
            multiprocesses.append(spec06_benchmarks.gobmk)
        elif benches[i] == '456.hmmer':
            print('--> 456.hmmer')
            multiprocesses.append(spec06_benchmarks.hmmer)
        elif benches[i] == '458.sjeng':
            print('--> 458.sjeng')
            multiprocesses.append(spec06_benchmarks.sjeng)
        elif benches[i] == '462.libquantum':
            print('--> 462.libquantum')
            multiprocesses.append(spec06_benchmarks.libquantum)
        elif benches[i] == '464.h264ref':
            print('--> 464.h264ref')
            multiprocesses.append(spec06_benchmarks.h264ref)
        elif benches[i] == '471.omnetpp':
            print('--> 471.omnetpp')
            multiprocesses.append(spec06_benchmarks.omnetpp)
        elif benches[i] == '473.astar':
            print('--> 473.astar')
            multiprocesses.append(spec06_benchmarks.astar)
        elif benches[i] == '483.xalancbmk':
            print('--> 483.xalancbmk')
            multiprocesses.append(spec06_benchmarks.xalancbmk)
        elif benches[i] == '600.perlbench_s':  #spec2017
            print('--> perlbench_s')
            multiprocesses.append(spec17_benchmarks.perlbench_s)
        elif benches[i] == '602.gcc_s':
            print('--> gcc_s')
            multiprocesses.append(spec17_benchmarks.gcc_s)
        elif benches[i] == '505.mcf_r':
            print('--> mcf_r')
            multiprocesses.append(spec17_benchmarks.mcf_r)
        elif benches[i] == '605.mcf_s':
            print('--> mcf_s')
            multiprocesses.append(spec17_benchmarks.mcf_s)
        elif benches[i] == '520.omnetpp_r':
            print('--> omnetpp_r')
            multiprocesses.append(spec17_benchmarks.omnetpp_r)
        elif benches[i] == '620.omnetpp_s':
            print('--> omnetpp_s')
            multiprocesses.append(spec17_benchmarks.omnetpp_s)
        elif benches[i] == '523.xalancbmk_r':
            print('--> xalancbmk_r')
            multiprocesses.append(spec17_benchmarks.xalancbmk_r)
        elif benches[i] == '623.xalancbmk_s':
            print('--> xalancbmk_s')
            multiprocesses.append(spec17_benchmarks.xalancbmk_s)
        elif benches[i] == '525.x264_r':
            print('--> x264_r')
            multiprocesses.append(spec17_benchmarks.x264_r)
        elif benches[i] == '625.x264_s':
            print('--> x264_s')
            multiprocesses.append(spec17_benchmarks.x264_s)
        elif benches[i] == '531.deepsjeng_r':
            print('--> deepsjeng_r')
            multiprocesses.append(spec17_benchmarks.deepsjeng_r)
        elif benches[i] == '631.deepsjeng_s':
            print('--> deepsjeng_s')
            multiprocesses.append(spec17_benchmarks.deepsjeng_s)
        elif benches[i] == '541.leela_r':
            print('--> leela_r')
            multiprocesses.append(spec17_benchmarks.leela_r)
        elif benches[i] == '641.leela_s':
            print('--> leela_s')
            multiprocesses.append(spec17_benchmarks.leela_s)
        elif benches[i] == '648.exchange2_s':
            print('--> exchange2_s')
            multiprocesses.append(spec17_benchmarks.exchange2_s)
        elif benches[i] == '557.xz_r':
            print('--> xz_r')
            multiprocesses.append(spec17_benchmarks.xz_r)
        elif benches[i] == '657.xz_s':
            print('--> xz_s')
            multiprocesses.append(spec17_benchmarks.xz_s)
        elif benches[i] == '503.bwaves_r':
            print('--> bwaves_r')
            multiprocesses.append(spec17_benchmarks.bwaves_r)
        elif benches[i] == '603.bwaves_s':
            print('--> bwaves_s')
            multiprocesses.append(spec17_benchmarks.bwaves_s)
        elif benches[i] == '507.cactuBSSN_r':
            print('--> cactuBSSN_r')
            multiprocesses.append(spec17_benchmarks.cactuBSSN_r)
        elif benches[i] == '607.cactuBSSN_s':
            print('--> cactuBSSN_s')
            multiprocesses.append(spec17_benchmarks.cactuBSSN_s)
        elif benches[i] == '508.namd_r':
            print('--> namd_r')
            multiprocesses.append(spec17_benchmarks.namd_r)
        elif benches[i] == '510.parest_r':
            print('--> parest_r')
            multiprocesses.append(spec17_benchmarks.parest_r)
        elif benches[i] == '511.povray_r':
            print('--> povray_r')
            multiprocesses.append(spec17_benchmarks.povray_r)
        elif benches[i] == '519.lbm_r':
            print('--> lbm_r')
            multiprocesses.append(spec17_benchmarks.lbm_r)
        elif benches[i] == '619.lbm_s':
            print('--> lbm_s')
            multiprocesses.append(spec17_benchmarks.lbm_s)
        elif benches[i] == '521.wrf_r':
            print('--> wrf_r')
            multiprocesses.append(spec17_benchmarks.wrf_r)
        elif benches[i] == '621.wrf_s':
            print('--> wrf_s')
            multiprocesses.append(spec17_benchmarks.wrf_s)
        elif benches[i] == '526.blender_r':
            print('--> blender_r')
            multiprocesses.append(spec17_benchmarks.blender_r)
        elif benches[i] == '527.cam4_r':
            print('--> cam4_r')
            multiprocesses.append(spec17_benchmarks.cam4_r)
        elif benches[i] == '627.cam4_s':
            print('--> cam4_s')
            multiprocesses.append(spec17_benchmarks.cam4_s)
        elif benches[i] == '628.pop2_s':
            print('--> pop2_s')
            multiprocesses.append(spec17_benchmarks.pop2_s)
        elif benches[i] == '538.imagick_r':
            print('--> imagick_r')
            multiprocesses.append(spec17_benchmarks.imagick_r)
        elif benches[i] == '638.imagick_s':
            print('--> imagick_s')
            multiprocesses.append(spec17_benchmarks.imagick_s)
        elif benches[i] == '544.nab_r':
            print('--> nab_r')
            multiprocesses.append(spec17_benchmarks.nab_r)
        elif benches[i] == '644.nab_s':
            print('--> nab_s')
            multiprocesses.append(spec17_benchmarks.nab_s)
        elif benches[i] == '549.fotonik3d_r':
            print('--> fotonik3d_r')
            multiprocesses.append(spec17_benchmarks.fotonik3d_r)
        elif benches[i] == '649.fotonik3d_s':
            print('--> fotonik3d_s')
            multiprocesses.append(spec17_benchmarks.fotonik3d_s)
        elif benches[i] == '554.roms_r':
            print('--> roms_r')
            multiprocesses.append(spec17_benchmarks.roms_r)
        elif benches[i] == '654.roms_s':
            print('--> roms_s')
            multiprocesses.append(spec17_benchmarks.roms_s)
        else:
            print("No recognized SPEC_CPU2017 benchmark selected! Exiting.")
            sys.exit(1)
elif args.bench:
    apps = args.bench.split("-")
    if len(apps) != args.num_cpus:
        print("number of benchmarks not equal to set num_cpus!")
        sys.exit(1)

    for app in apps:
        try:
            if get_runtime_isa() == ISA.ARM:
                exec(
                    "workload = %s('arm_%s', 'linux', '%s')"
                    % (app, args.arm_iset, args.spec_input)
                )
            else:
                # TARGET_ISA has been removed, but this is missing a ], so it
                # has incorrect syntax and wasn't being used anyway.
                exec(
                    "workload = %s(buildEnv['TARGET_ISA', 'linux', '%s')"
                    % (app, args.spec_input)
                )
            multiprocesses.append(workload.makeProcess())
        except:
            print(
                "Unable to find workload for %s: %s"
                % (get_runtime_isa().name(), app),
                file=sys.stderr,
            )
            sys.exit(1)
elif args.cmd:
    multiprocesses, numThreads = get_processes(args)
else:
    print("No workload specified. Exiting!\n", file=sys.stderr)
    sys.exit(1)


(CPUClass, test_mem_mode, FutureClass) = Simulation.setCPUClass(args)
CPUClass.numThreads = numThreads

# Check -- do not allow SMT with multiple CPUs
if args.smt and args.num_cpus > 1:
    fatal("You cannot use SMT with multiple CPUs!")

np = args.num_cpus
mp0_path = multiprocesses[0].executable
system = System(
    cpu=[CPUClass(cpu_id=i) for i in range(np)],
    mem_mode=test_mem_mode,
    mem_ranges=[AddrRange(args.mem_size)],
    cache_line_size=args.cacheline_size,
)

if numThreads > 1:
    system.multi_thread = True

# Create a top-level voltage domain
system.voltage_domain = VoltageDomain(voltage=args.sys_voltage)

# Create a source clock for the system and set the clock period
system.clk_domain = SrcClockDomain(
    clock=args.sys_clock, voltage_domain=system.voltage_domain
)

# Create a CPU voltage domain
system.cpu_voltage_domain = VoltageDomain()

# Create a separate clock domain for the CPUs
system.cpu_clk_domain = SrcClockDomain(
    clock=args.cpu_clock, voltage_domain=system.cpu_voltage_domain
)

# If elastic tracing is enabled, then configure the cpu and attach the elastic
# trace probe
if args.elastic_trace_en:
    CpuConfig.config_etrace(CPUClass, system.cpu, args)

# All cpus belong to a common cpu_clk_domain, therefore running at a common
# frequency.
for cpu in system.cpu:
    cpu.clk_domain = system.cpu_clk_domain

if ObjectList.is_kvm_cpu(CPUClass) or ObjectList.is_kvm_cpu(FutureClass):
    if buildEnv["USE_X86_ISA"]:
        system.kvm_vm = KvmVM()
        system.m5ops_base = 0xFFFF0000
        for process in multiprocesses:
            process.useArchPT = True
            process.kvmInSE = True
    else:
        fatal("KvmCPU can only be used in SE mode with x86")

# Sanity check
if args.simpoint_profile:
    if not ObjectList.is_noncaching_cpu(CPUClass):
        fatal("SimPoint/BPProbe should be done with an atomic cpu")
    if np > 1:
        fatal("SimPoint generation not supported with more than one CPUs")

for i in range(np):
    # pdb.set_trace()
    if args.smt:
        system.cpu[i].workload = multiprocesses
    elif len(multiprocesses) == 1:
        system.cpu[i].workload = multiprocesses[0]
    else:
        system.cpu[i].workload = multiprocesses[i]

    if args.simpoint_profile:
        system.cpu[i].addSimPointProbe(args.simpoint_interval)

    if args.checker:
        system.cpu[i].addCheckerCpu()

    if args.bp_type:
        bpClass = ObjectList.bp_list.get(args.bp_type)
        system.cpu[i].branchPred = bpClass()

    if args.indirect_bp_type:
        indirectBPClass = ObjectList.indirect_bp_list.get(
            args.indirect_bp_type
        )
        system.cpu[i].branchPred.indirectBranchPred = indirectBPClass()

    system.cpu[i].createThreads()

MemClass = Simulation.setMemClass(args)
system.membus = SystemXBar()
system.system_port = system.membus.cpu_side_ports
CacheConfig.config_cache(args, system)
# MemConfig.config_mem(args, system)

# Dramsim3 
system.mem_ctrl = DRAMsim3()
system.mem_ctrl.configFile = args.ds_config
system.mem_ctrl.filePath = "./m5out"
system.mem_ctrl.range = system.mem_ranges[0]
system.mem_ctrl.port = system.membus.mem_side_ports

config_filesystem(system, args)

system.workload = SEWorkload.init_compatible(mp0_path)

if args.wait_gdb:
    system.workload.wait_for_remote_gdb = True

root = Root(full_system=False, system=system)
Simulation.run(args, root, system, FutureClass)
