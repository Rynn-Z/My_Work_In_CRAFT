base_path=/root/spec2017/benchspec/CPU
dest_path=/root/gem5/configs/spec2017
for i in ${base_path}/*
do
	if [ -d "${i}" ]; then
		echo ${i#*CPU/}
		cp -r ${i}/run/*ref*  ${dest_path}/${i#*CPU/}/
	
	fi
done
