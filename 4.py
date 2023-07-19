import math
a = float(input("Введите коэффицент 'a': "))
b = float(input("Введите коэффицент 'b': "))
c = float(input("Введите коэффицент 'c': "))

D = (b ** 2 - 4 * c * a)
if D < 0:
    print("Корней нет")
elif D == 0:
    x = (- b) / (2 * a)
    print(x)
else:
    x1 = (- b + math.sqrt(D)) / (2 * a)
    x2 = (- b - math.sqrt(D)) / (2 * a)
    print(x1, x2)
