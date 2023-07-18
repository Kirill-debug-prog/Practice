a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

sym = 0
for i in range(a, b + 1):
    sym += i
print(sym)
