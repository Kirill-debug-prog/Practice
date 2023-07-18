import itertools


def find_combinations(numbers, target_sum):
    combinations = []
    for i in range(1, len(numbers) + 1):
        for combination in itertools.combinations(numbers, i):
            if sum(combination) == target_sum:
                combinations.append(combination)
    return list(set(combinations))


numbers = int(input("Введите число: "))
n = [x for x in range(1, numbers + 1)]
target_sum = int(input("Введите целевую сумму:"))
combinations = find_combinations(n, target_sum)
print("Уникальные комбинации суммы", target_sum, ":")
for combination in combinations:
    print(combination)
