#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Use: $0 <method> <obstacles_folder>"
    echo "  <method> - a: A-STAR (heuristic: Euclidean distance), b: BFS, d: DFS."
    echo "  <obstacles_folder> - name of the folder inside data where tgf files are"
    exit 1
fi

method="$1"
obstacles_folder="$2"

for i in {1..100};
do
  python graph.py $method data/$obstacles_folder/$i.tgf;
done