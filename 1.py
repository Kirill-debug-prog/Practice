import csv

data = [
    ["Книга", "Автор", "Год выпуска"],
    ["Tarzan", "Edgar Burroughs", "1990"],
    ["The Hobbit", "John R.R, Tolkien", "1937"],
    ["Harry Potter and the Philosopher's Stone", 
     "Roman, J.K. Rowling", "1997"],
    ["Harry Potter and the Deathly Hallows Part 1", 
     "Joanne Rowling", "2007"]
]

filename = "books.csv"
with open(filename, mode="w", newline ='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
print("Файл создан: ", filename)
