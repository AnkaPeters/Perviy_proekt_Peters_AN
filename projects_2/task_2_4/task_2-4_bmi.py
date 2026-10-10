weight = float(input("Введите ваш вес (кг): "))
height = float(input("Введите ваш рост (м): "))

bmi = weight / (height ** 2)

print(f"--- Отчет о состоянии здоровья ---\n\
Рост: \t{height} м\n\
Вес: \t {weight} кг \n\
Индекс массы тела пациента: {bmi:.2f}")

