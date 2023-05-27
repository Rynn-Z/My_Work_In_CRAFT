# ./crazywang.sh > result1.csv

base_path=~/gem5/configs/spec2017

for i in $base_path/*
do

for j in ${i}/prof/*
do

if [ -f "${j}/stats.txt" ]; then
echo -n ${j#*prof/}

for k in `cat ${j}/stats.txt | grep -E "mem_ctrl.*total|simTicks" | awk '{print $2}'`
do

echo -n ", "
echo -n ${k}

done
echo " "

fi

done

done

