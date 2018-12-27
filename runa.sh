j=$1
index=$2
flag=$3
#echo $index
#echo "$HOME/Desktop/data/J${j}/j${j}.${index}.in"

if [ -f "$HOME/Desktop/data/J${j}/j${j}.${index}.in" ]
then
	echo "$index"
else
	ls -l   "$HOME/Desktop/data/J${j}/j${j}.${index}.in" 
	exit 0 
fi

cat ~/Desktop/data/J${j}/j${j}.${index}.in   | python  j0${j}.py   > /tmp/a.txt ;

if [ $flag =  "1" ]; then
	echo "========================================"
	echo "测试输入" 
	cat  ~/Desktop/data/J${j}/j${j}.${index}.in ;
	echo "标准结果"
	cat ~/Desktop/data/J${j}/j${j}.${index}.out
	echo "程序运行结果"
	cat /tmp/a.txt ;
	echo "========================================"

fi

diff /tmp/a.txt   ~/Desktop/data/J${j}/j${j}.${index}.out

