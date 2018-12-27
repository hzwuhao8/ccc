j=$1
index=$2
flag=$3
echo $index
cat ~/Desktop/data/J1/j1.${index}.in   | python  j0${j}.py   > /tmp/a.txt ;

if [ $flag =  "1" ]; then
	cat  ~/Desktop/data/J${j}/j${j}.${index}.in ;
	cat ~/Desktop/data/J${j}/j${j}.${index}.out
	cat /tmp/a.txt ;
fi

diff /tmp/a.txt   ~/Desktop/data/J${j}/j${j}.${index}.out

