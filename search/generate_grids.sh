#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Use: $0 <obstacles>"
    exit 1
fi

obstacles="$1"

# Verify if the directory $obstacles exists, otherwise, it creates
if [ ! -d "$obstacles" ]; then
    mkdir -p "data/$obstacles"
fi

for i in {1..100};
do
    python robot.py 100 100 "$obstacles" > "data/$obstacles/$i.tgf";
done
