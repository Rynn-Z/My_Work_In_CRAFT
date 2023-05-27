#!/bin/bash
echo $1
target=""
#**************************** benchmark name ************************************
if [ $1 = "500" -o $1 = "perlbench_r" -o $1 = "500.perlbench_r" ]; then
        target=500.perlbench_r 
elif [ $1 = "502" -o $1 = "gcc_r" -o $1 = "502.gcc_r" ]; then
        target=502.gcc_r 
elif  [ $1 = "505" -o $1 = "mcf_r" -o $1 = "505.mcf_r" ]; then
        target=505.mcf_r 
elif  [ $1 = "520" -o $1 = "omnetpp_r" -o $1 = "520.omnetpp_r" ]; then
        target=520.omnetpp_r 
elif  [ $1 = "523" -o $1 = "xalancbmk_r" -o $1 = "523.xalancbmk_r" ]; then
        target=523.xalancbmk_r 
elif  [ $1 = "525" -o $1 = "x264_r" -o $1 = "525.x264_r" ]; then
        target=525.x264_r 
elif  [ $1 = "531" -o $1 = "deepsjeng_r" -o $1 = "531.deepsjeng_r" ]; then
        target=531.deepsjeng_r 
elif  [ $1 = "541" -o $1 = "leela_r" -o $1 = "541.leela_r" ]; then
        target=541.leela_r 
elif  [ $1 = "548" -o $1 = "exchange2_r" -o $1 = "548.exchange2_r" ]; then
        target=548.exchange2_r 
elif  [ $1 = "557" -o $1 = "xz_r" -o $1 = "557.xz_r" ]; then
        target=557.xz_r 
elif  [ $1 = "600" -o $1 = "perlbench_s" -o $1 = "600.perlbench_s" ]; then
        target=600.perlbench_s 
elif  [ $1 = "602" -o $1 = "gcc_s" -o $1 = "602.gcc_s" ]; then
        target=602.gcc_s 
elif  [ $1 = "605" -o $1 = "mcf_s" -o $1 = "605.mcf_s" ]; then
        target=605.mcf_s 
elif  [ $1 = "620" -o $1 = "omnetpp_s" -o $1 = "620.omnetpp_s" ]; then
        target=620.omnetpp_s 
elif  [ $1 = "623" -o $1 = "xalancbmk_s" -o $1 = "623.xalancbmk_s" ]; then
        target=623.xalancbmk_s 
elif  [ $1 = "625" -o $1 = "x264_s" -o $1 = "625.x264_s" ]; then
        target=625.x264_s 
elif  [ $1 = "631" -o $1 = "deepsjeng_s" -o $1 = "631.deepsjeng_s" ]; then
        target=631.deepsjeng_s 
elif  [ $1 = "641" -o $1 = "leela_s" -o $1 = "641.leela_s" ]; then
        target=641.leela_s 
elif  [ $1 = "648" -o $1 = "exchange2_s" -o $1 = "648.exchange2_s" ]; then
        target=648.exchange2_s 
elif  [ $1 = "657" -o $1 = "xz_s" -o $1 = "657.xz_s" ]; then
        target=657.xz_s
elif  [ $1 = "503" -o $1 = "bwaves_r" -o $1 = "503.bwaves_r" ]; then
	target=503.bwaves_r
elif  [ $1 = "507" -o $1 = "cactuBSSN_r" -o $1 = "507.cactuBSSN_r" ]; then
	target=507.cactuBSSN_r
elif  [ $1 = "508" -o $1 = "namd_r" -o $1 = "508.namd_r" ]; then
        target=508.namd_r
elif  [ $1 = "510" -o $1 = "parest_r" -o $1 = "510.parest_r" ]; then
	target=510.parest_r
elif  [ $1 = "511" -o $1 = "povray_r" -o $1 = "511.povray_r" ]; then
	target=511.povray_r
elif  [ $1 = "519" -o $1 = "lbm_r" -o $1 = "519.lbm_r" ]; then
	target=519.lbm_r
elif  [ $1 = "521" -o $1 = "wrf_r" -o $1 = "521.wrf_r" ]; then
	target=521.wrf_r
elif  [ $1 = "526" -o $1 = "blender_r" -o $1 = "526.blender_r" ]; then
	target=526.blender_r
elif  [ $1 = "527" -o $1 = "cam4_r" -o $1 = "527.cam4_r" ]; then
	target=527.cam4_r
elif  [ $1 = "538" -o $1 = "imagick_r" -o $1 = "538.imagick_r" ]; then
	target=538.imagick_r
elif  [ $1 = "544" -o $1 = "nab_r" -o $1 = "544.nab_r" ]; then
	target=544.nab_r
elif  [ $1 = "549" -o $1 = "fotonik3d_r" -o $1 = "549.fotonik3d_r" ]; then
	target=549.fotonik3d_r
elif  [ $1 = "554" -o $1 = "roms_r" -o $1 = "554.roms_r" ]; then
	target=554.roms_r
elif  [ $1 = "603" -o $1 = "bwaves_s" -o $1 = "603.bwaves_s" ]; then
	target=603.bwaves_s
elif  [ $1 = "607" -o $1 = "cactuBSSN_s" -o $1 = "607.cactuBSSN_s" ]; then
	target=607.cactuBSSN_s
elif  [ $1 = "619" -o $1 = "lbm_s" -o $1 = "619.lbm_s" ]; then
	target=619.lbm_s
elif  [ $1 = "621" -o $1 = "wrf_s" -o $1 = "621.wrf_s" ]; then
	target=621.wrf_s
elif  [ $1 = "627" -o $1 = "cam4_s" -o $1 = "627.cam4_s" ]; then
	target=627.cam4_s
elif  [ $1 = "628" -o $1 = "pop2_s" -o $1 = "628.pop2_s" ]; then
	target=628.pop2_s
elif  [ $1 = "638" -o $1 = "imagick_s" -o $1 = "638.imagick_s" ]; then
	target=638.imagick_s
elif  [ $1 = "644" -o $1 = "nab_s" -o $1 = "644.nab_s" ]; then
	target=644.nab_s
elif  [ $1 = "649" -o $1 = "fotonik3d_s" -o $1 = "649.fotonik3d_s" ]; then
	target=649.fotonik3d_s
elif  [ $1 = "654" -o $1 = "roms_s" -o $1 = "654.roms_s" ]; then
	target=654.roms_s
else
	echo "input wrong!"
	exit
fi

echo $target
case_name=${target:4}
echo $case_name
EXE=${case_name}_base.mytest-m64

# EXE=${target}_base.mytest-m64

#========================================================
EXE_BASE_PATH=/root/benchmark/spec2017/benchspec/CPU/${target}/run/run_base_test_mytest-m64.0000
OUT_BASE_PATH=/root/gem5old/configs/spec2017
if [ ! -d $OUT_BASE_PATH ];then
    mkdir $OUT_BASE_PATH
fi

PATH_TO_GEM5=/root/gem5old

#Four crucial dir
SE_OUT_DIR_BASE=${OUT_BASE_PATH}/$target
ii
if [ ! -d $SE_OUT_DIR_BASE ];then
    mkdir $SE_OUT_DIR_BASE
fi

SE_OUT_DIR_INIT=${OUT_BASE_PATH}/${target}/bbv
SE_OUT_DIR_CHECKPOINT=${OUT_BASE_PATH}/${target}/ckpt
SE_OUT_DIR_RELOAD=${OUT_BASE_PATH}/${target}/restore
SE_OUT_DIR_RELOAD_PROF=${OUT_BASE_PATH}/${target}/prof
SE_OUT_DIR_SIMPOINT=${OUT_BASE_PATH}/${target}/simpoint
SE_Simpoint_PATH=${OUT_BASE_PATH}/${target}/simpoint

#simpoint and weight
SE_simpoint_file_path=${SE_Simpoint_PATH}/simpoints
SE_weight_file_path=${SE_Simpoint_PATH}/weights

#output and error file 
OUTPUT_PATH=${OUT_BASE_PATH}/${target}/$output
ERROR_PATH=${OUT_BASE_PATH}/${target}/$errout



############------  executable file  -----##########
# update!
interval_length=300000000  #300M
warmup_length=10000000  #10M

echo $OUTPUT_PATH

SE_ELF_ROUTE=$EXE
SE_INPUT_ROUTE=$input
OPTIONS=$args
############==========--------===========############
