import csv

with open('books.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)
    start_year = int(input("Введите начальный год: "))
    end_year = int(input("Введите конечный год: "))
    if start_year > end_year:
        print("Некоректный запрос! Начальный год должен быть меньше или равен конечному году")
    else:
        for row in reader:
            year = int(row[2])
            if start_year<=year<=end_year:
                print(f"Название{row[0]}, Автор: {row[1]}, Год: {row[2]}")
