solution_volume = float(input("Введите нужный объем раствора (в мл): "))

massa_NaCl = solution_volume * 0.009
water_volume = solution_volume

with open("D:/AU/python/projects_2/recipe.txt", "w", encoding="utf-8") as file:
    file.write(f"ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n\
-------------------------\n\
Общий объем:\t{solution_volume} мл\n\
Масса соли:\t{massa_NaCl:.2f} мг\t\n\
Объем воды:\t{water_volume} мл")
