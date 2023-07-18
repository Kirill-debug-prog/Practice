string = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
vowels = "аеёиоуыюя"
choice = {letter: True if letter in vowels else False for letter in string}
print(choice)
