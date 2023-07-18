n = int(input("Введите число: "))
non_prime_numbers = [x for x in range(2, n+1)
                     if any(x % i == 0 for i in range(2, int(x ** 0.5) + 1))]
print(non_prime_numbers)
