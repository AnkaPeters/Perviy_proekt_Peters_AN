number_of_capsules = int(input("Введите общее количество произведенных капсул: "))
capsules_in_package = int(input("Введите количество капсул в одной упаковке: "))

full_packages = number_of_capsules // capsules_in_package
remain_quantity = number_of_capsules % capsules_in_package

print(f"--- Отчет фасовочного цеха ---\n\
Полных упаковок: \t {full_packages} \n\
Остаток капсул: \t {remain_quantity} ")

