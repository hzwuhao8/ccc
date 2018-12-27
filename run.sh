j=$1


if [ -f "j0${j}.py" ]
then
	echo "run"
else
	exit 
fi

for index in `seq 1 13`
do
 bash runa.sh $j $index 0
 if [ $? != "0" ]; then
	bash runa.sh $j $index 1
 fi
done

for index in "sample1" "sample2"
do
 bash runa.sh $j $index 0
 if [ $? != "0" ]; then
        bash runa.sh $j $index 1
 fi

done

