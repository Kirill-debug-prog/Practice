num=input("Введите число: ")
n=len(num)
sum=0
for digit in num:
    sum+=int(digit)**n
if sum==int(num):
    print(num, "является числом Армстронга")
else:
    print(num, "не является числом Армстронга")
