flag=$1
fin=$2
fout=$3
myp=$4

#echo "runa.sh  flag  data out  myp"

if [ $flag =  "1" ]; then
	echo "flag=${flag} fin=${fin} fout=${fout} myp=${myp}"
fi

if [ -f "$fin" ]
then
	echo "$fin"
else
	echo  "$fin" 
	exit 0 
fi

cat "$fin"   | python3  $myp   > /tmp/a.txt ;

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

diff --strip-trailing-cr  /tmp/a.txt   "$fout"

