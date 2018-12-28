j=$1


if [ -f "j0${j}.py" ]
then
	echo "run"
else
	echo  "python 程序不存在 j0${j}.py"
	exit 
fi

for fin in  $(ls /$HOME/Desktop/data/J${j}/*.in)
do
 fout="${fin/in/out}"
 bash runa.sh $j 0 $fin $fout 
 if [ $? != "0" ]; then
	bash runa.sh $j 1  $index  $fin $fout
	exit
 fi
done


