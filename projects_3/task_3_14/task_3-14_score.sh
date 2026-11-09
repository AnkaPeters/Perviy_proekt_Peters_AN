#!/bin/bash

echo "студенты с оценкой выше 80:"
awk '$2 > 80 {print $1, $2}' students.txt

echo "студенты с оценкой ниже 70:"
awk '$2 < 70 {print $1, $2}' students.txt

echo "первая строка:"
awk 'NR == 1 {print; exit}' students.txt
