score = int(input("Введите кол-во очкоа команды за игру: "))
if score == 3:
    print("Выигрыш")
elif score == 1:
    print("Ничья")
elif score == 0:
    print("Проигрышь")
else:
    print("Некорректное кол-во очков")
