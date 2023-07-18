import random

wins = 0
losses = 0
consecutive_losses = 0

while consecutive_losses < 3:
    guess = input("Орёл или решка? (0 - орёл, 1 - решка, "
                  "любое другое число - выход): ")
    if guess == "0":
        user_choice = "орёл"
    elif guess == "1":
        user_choice = "решка"
    else:
        break

    computer_chose = random.choice(["орёл", "решка"])
    print("Вы выбрали", user_choice)
    print("Компьютер выбрал", computer_chose)

    if user_choice == computer_chose:
        print("Вы выиграли")
        wins += 1
        consecutive_losses = 0
    else:
        print("Вы проиграли")
        losses += 1
        consecutive_losses += 1

    print("Выигрышь", wins)
    print("Проигрыши", losses)
    print("Поражения подряд", consecutive_losses)

print("Игра окончена")
