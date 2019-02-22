#!/bin/bash

# bash control flow

a=0

# if-statement
if [ $a -gt 0 ]; then
      echo "yes"
else
      echo "no"
fi

# case-statement
a="a"

case $a in 
   a)    echo "a" ;;
   x)    echo "x" ;;
   [yz]) echo "y or z" ;;
   *)    echo "else" ;;
esac