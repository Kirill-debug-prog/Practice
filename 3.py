num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))

if num1 >= num2 and num1 >= num3:
    print(num1, "является наибольшим")
    if num2 >= num3:
        print("Числа по убыванию", num1, num2, num3)
    else:
        print("Числа по убыванию", num1, num3, num2)

elif num2 >= num1 and num2 >= num3:
    print(num2, "является наибольшим")
    if num1 >= num3:
        print("Числа по убыванию", num2, num1, num3)
    else:
        print("Числа по убыванию", num2, num3, num1)

else:
    print(num3, "является наибольшим")
    if num1 >= num3:
        print("Числа по убыванию", num3, num1, num2)
    else:
        print("Числа по убыванию", num3, num2, num1)
