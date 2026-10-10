operator_name = input('Введите имя оператора: ')
pressure = input('Введите текущее значение давления (Па): ')

with open("D:/AU/python/projects_2/sensor_log.txt", "w", encoding="utf-8") as file:
    file.write(f"Оператор:\t{operator_name}\n\
Значение:\t{pressure}\n")

print("\nФайл 'sensor_log.txt' успешно сформирован!")
    
