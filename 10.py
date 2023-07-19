num = float(input("Введите вещественное число"))
formatted_number = "{:,.2f}".format(num)
print(formatted_number.replace(",", "."))
