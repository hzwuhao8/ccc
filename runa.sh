j=$1
flag=$2
fin=$3
fout=$4
#echo $index
#echo "$HOME/Desktop/data/J${j}/j${j}.${index}.in"

if [ -f "$fin" ]
then
	echo "$fin"
else
	echo  "$fin" 
	exit 0 
fi

cat "$fin"   | python3  j0${j}.py   > /tmp/a.txt ;

if [ $flag =  "1" ]; then
	echo "========================================"
	echo "测试输入" 
	cat  "$fin" ;
	echo "标准结果"
	cat  "$fout"
	echo "程序运行结果"
	cat /tmp/a.txt ;
	echo "========================================"

fi

diff /tmp/a.txt   "$fout"

