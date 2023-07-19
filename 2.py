import csv

num_records = int(input("Скоько записей вы хотите добавить? "))
records = []
for _ in range(num_records):
    books = input("Введите название книги: ")
    authors = input("Введите имя автора: ")
    years = input("Введите год выпуска: ")
    records.append([books, authors, years])

with open("books.csv", mode="a") as file:
    writer = csv.writer(file)
    writer.writerows(records)

    author = input("Введите автора книги: ")
    with open("books.csv", mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        books = []
        for row in reader:
            if row[1] == author:
                books.append(row[2])

    if books:
        print("Книга автора", author + ":", ",".join(books))
    else:
        print("Нет книг автора", author)
