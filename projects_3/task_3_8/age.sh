#!/bin/bash

# Присваивание
readonly CURRENT_YEAR=2026
read -p "Введите год рождения: " BIRTH_YEAR

# Вычисление (Арифметика)
AGE=$((CURRENT_YEAR - BIRTH_YEAR))

# Вывод с интерполяцией
echo "Текущий год: $CURRENT_YEAR"
echo "Ваш примерный возраст: $AGE"
