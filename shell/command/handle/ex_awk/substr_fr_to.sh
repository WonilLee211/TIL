if [ "$#" != "3" ]; then
	echo "check your arguments!!!"
	echo "args[0] : str"
	echo "args[1] : fr_idx"
	echo "args[2] : to_idx"
fi
STR=$1
FR_IDX=$2
TO_IDX=`expr $3 - $2`
echo $STR | awk -F " " '{ print substr($1, C1, C2) }' C1="$FR_IDX" C2="$TO_IDX"
