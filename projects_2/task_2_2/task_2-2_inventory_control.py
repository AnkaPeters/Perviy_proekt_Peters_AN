print('Введите наименование нового реактива')
name_new_reagent = input()
print('Введите количество поступившего реактива')
quantity = int(input())

print(f'Реактив {name_new_reagent} поступил на склад в количестве {quantity} шт.')

f = open("D:/AU/python/projects_2/inventory.txt", "w", encoding="utf-8")
print(f'Реактив {name_new_reagent} поступил на склад в количестве {quantity} шт.', file = f)
f.close()
