dna = input("Введите последовательность ДНК: ").upper()

# Подсчёт нуклеотидов
count_A = dna.count("A")
count_T = dna.count("T")
count_G = dna.count("G")
count_C = dna.count("C")

len = len(dna)

percent_A = count_A / len * 100
percent_T = count_T / len * 100
percent_G = count_G / len * 100
percent_C = count_C / len * 100

print(f"Последовательность в верхнем регистре: {dna} \n\n\
Подсчёт нуклеотидов:\n\
A: {count_A}\n\
T: {count_T}\n\
G: {count_G}\n\
C: {count_C}\n\n\
Общая длина: {len} нуклеотидов")

print(f"\nПроцентное содержание каждого нуклеотида:\n\
A: {percent_A:.2f}%\n\
T: {percent_T:.2f}%\n\
G: {percent_G:.2f}%\n\
C: {percent_C:.2f}%")
