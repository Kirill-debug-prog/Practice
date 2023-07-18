string = input("Введите строку: ")
number_of_letters = {char: string.count(char)
                     for char in string if char.isalpha()}
print(number_of_letters)
