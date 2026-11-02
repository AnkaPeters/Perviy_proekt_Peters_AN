#!/bin/bash

printf "%-19s %-7s %-7s %-7s %-7s\n" "Файл" "A" "T" "G" "C"

for file in *.fasta; do
    if [ ! -s "$file" ]; then
        continue;
    fi
    grep -v "^>" "$file" > output.txt
    tr -d '\n' < output.txt > output1.txt
    printf "%-15s %-7s %-7s %-7s %-7s\n" "$file" "$(grep -o "A" output1.txt | wc -l)" "$(grep -o "T" output1.txt | wc -l)" "$(grep -o "G" output1.txt | wc -l)" "$(grep -o "C" output.txt | wc -l)"
done
