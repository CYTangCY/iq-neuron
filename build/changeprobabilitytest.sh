#!/bin/sh
i=1
time=1000
while [ $i -le $time ]
do
    ./libiq < ../inputs/session.txt
    python3 changepro.py
    i=$(($i+1))
    echo "已經跑了$i次囉"
done    

