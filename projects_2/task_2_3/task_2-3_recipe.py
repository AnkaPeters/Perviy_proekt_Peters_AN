name_nutrient_medium = input('Введите название питательной среды: ')
agar_concentration = input('Введите концентрацию агара (%): ')
sterilization_temperature = input('Введите температуру стерилизации (°C): ')

with open("D:/AU/python/projects_2/recipe.txt", "w", encoding="utf-8") as guide:
    guide.write(f"{name_nutrient_medium}\nконцентрация агара (%): {agar_concentration}\n\
температура стерилизации (°C): {sterilization_temperature}\n")

print("\nФайл 'recipe.txt' успешно сформирован!")
    
