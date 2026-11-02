#!/bin/bash

#создание файлов

for i in {1..10}; do
    touch test$i.txt
done

#удаление файлов

i=10
while [ "$i" -gt 0 ]; do
    rm test$i.txt
    ((i--))
done
