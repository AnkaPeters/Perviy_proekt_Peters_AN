#!/bin/bash

echo "названия товаров:"
awk -F "," '{print $2}' data.csv

echo "товары дороже 20:"
awk -F "," '$3 > 20 {print $2, $3}' data.csv

echo "Общая стоимость:"
awk -F "," '{sum += $3; n++} END {print sum}' data.csv
