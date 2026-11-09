#!/bin/bash

echo "Находим сумму всех оценок:"
awk '{sum += $2; n++} END {print sum}' students.txt

echo "Находим среднее арифметическое оценок:"
awk '{sum += $2; n++} END {print sum/n}' students.txt

echo "Находим максимальную оценку:"
awk 'NR==1{max=$2} $2>max{max=$2} END{print max}' students.txt
