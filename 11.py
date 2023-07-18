string = input()
unique_letters = {char: string.count(char)
                  for char in set(string) if char.isalpha()}
print(unique_letters)
