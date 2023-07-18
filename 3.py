def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 1:
            return False
        return True


def find_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes


start = int(input("Введите начало диапозона: "))
end = int(input("Введите конец диапозона: "))
primes = find_primes(start, end)
print("Простые числа в заданном диапозоне")
for prime in primes:
    print(prime)
