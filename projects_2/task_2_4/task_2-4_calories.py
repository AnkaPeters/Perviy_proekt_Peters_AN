protein = int(input('Введите массу белков в продукте (г): '))
fat = int(input('Введите массу жиров в продукте (г): '))
carbohydrate = int(input('Введите массу углеводов в продукте (г): '))

calorie = 4 * (protein + carbohydrate) + 9 * fat

print(f'\nОбщая калорийность продукта составляет {calorie} кк')
