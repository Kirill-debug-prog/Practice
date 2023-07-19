num = (input("Введите натуральное число, в котором все цифры различны: "))
max_digit = max(num)
from_end = num[::-1].index(max_digit) + 1
from_start = num.index(max_digit)
print("Порядковый номер максимальной цифры от конца числа", from_end)
print("Порядковый номер максимальной цифры от начала числа", from_start)
