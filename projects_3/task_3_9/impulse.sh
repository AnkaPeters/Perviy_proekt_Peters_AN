#!/bin/bash

read -p "Введите имя гена: " Gen_name
read -p "Введите уровень его экспрессии (целое число): " Expression

if [[ -n "$Gen_name" && "$Expression" -gt 0 ]]; then
    echo "Экспрессия гена $Gen_name составляет $Expression единиц"
else
    echo "Недостаточно входящих данных"
fi
