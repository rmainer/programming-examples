#!/bin/bash

# needs Bash version 4

function min() {
	if [ $1 -le $2 -a $1 -le $3 ]; then
		echo $1
	elif [ $2 -le $1 -a $2 -le $3 ]; then
		echo $2
	else
		echo $3
	fi
}

function levenshtein() {
	declare -A d
	local w1=${1,,}
	local w2=${2,,}
	local n1=$(( $(echo -n $w1 | wc -c) + 1 ))
	local n2=$(( $(echo -n $w2 | wc -c) + 1 ))

	for ((y=0;y<n1;y++)) do
		for ((x=0;x<n2;x++)) do
			d[$y,$x]=0
		done
	done
	for ((y=1;y<n1;y++)) do
		d[$y,0]=$y
	done
	for ((x=1;x<n2;x++)) do
		d[0,$x]=$x 
	done

	for ((y=1;y<n1;y++)) do
		for ((x=1;x<n2;x++)) do
			if [ ${w1:$(($y-1)):1} = ${w2:$(($x-1)):1} ]; then
				d[$y,$x]=${d[$(($y-1)),$(($x-1))]}
			else
				d[$y,$x]=$(( $(min ${d[$(($y-1)),$(($x-1))]} ${d[$(($y-1)),$x]} ${d[$y,$(($x-1))]}) + 1 ))
			fi
		done
	done

	echo ${d[$(($n1-1)),$(($n2-1))]}
}


levenshtein "Roman" "Ramo"