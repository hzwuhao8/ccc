mydir=$1
ext=$2
myp=$3

echo " run.sh  data_dir  ext xxx.py"
echo "mydir=${mydir} ext=${ext}  myp=${myp}"
if [ -f "$myp" ]
then
	echo "run"
else
	echo  "python 程序不存在 $myp"
	exit 
fi

for fin in  $(ls ${mydir}*.${ext})
do
 fout="${fin/in/out}"
 fout="${fin/data/out}"
 bash runa.sh  0 $fin $fout  $myp
 if [ $? != "0" ]; then
	bash runa.sh  1 $fin $fout  $myp
	#exit
 else
	echo "ok"
 fi
done


