donor = input("Введите фенотип группы крови донора (I, II, III, IV): ").strip().upper()
recepient = input("Введите фенотип группы крови рецепиента (I, II, III, IV): ").strip().upper()

if donor == recepient or donor == 'I':
    print("Переливание возможно")
else:
    print("Переливание невозможно")
