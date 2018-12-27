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
	cat  ~/Desktop/data/J${j}/j${j}.${index}.in ;
	cat ~/Desktop/data/J${j}/j${j}.${index}.out
	cat /tmp/a.txt ;
fi

diff /tmp/a.txt   ~/Desktop/data/J${j}/j${j}.${index}.out

