n = int(input("Введите список чисел: "))
num = [x ** 2 for x in range(2, n + 1)
       if any(x % i == 0 for i in range(2, int(x ** 2) + 1))]
print(num)
