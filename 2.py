TV = ["Молодёжка", "Игра престолов", "Импровизация", "Comydy"]
print("Текущий список передач: ")
for show in TV:
    print(show)

new_shows = input('\n'"Введите название новой передачи: ")
position = int(input("Введите позицию, "
                     "на которую нужно вставить новую передачу "
                     "(от1 до 5): "))

TV.insert(position - 1, new_shows)

print("Новый список передач: ")
for show in TV:
    print(show)
