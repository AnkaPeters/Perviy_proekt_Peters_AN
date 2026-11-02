#!/bin/bash

# Описываем функцию
check_root() {
     if [ "$EUID" -ne 0 ]; then
        echo "Ошибка: скрипт должен запускаться от имени суперпользователя!!!"
        return 1
    fi
}

# Вызываем функцию
check_root
