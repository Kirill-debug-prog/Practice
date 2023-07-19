import random 

colors = ["красный", "синий", "черный",
          "зеленый", "желтый", "ораньжевый"]
program_choice = random.choice(colors)

print("Выберите один из следующих цветов")
for color in colors:
    print(color)

user_choice = input("Ваш выбор: ")
while user_choice != program_choice:
    print("Не угадали! Попробуйте еще раз")
    if colors.index(program_choice) > colors.index(user_choice):
        print("Правильный цвет находится ближе к началу списка")
    else:
        print("Правильный ответ находится ближе к концу списка")
    user_choice = input("Ваш выбор")

print("Отлично! Вы угадали цвет.")
