number = int(input("Введите число: "))
number_str = str(number)
sorted_str = sorted(number_str, reverse=True)
max_number = int(''.join(sorted_str))
print(max_number)
