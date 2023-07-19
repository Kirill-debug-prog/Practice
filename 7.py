def permutation(List):
    if len(List) == 0:
        return [[]]
    elif len(List) == 1:
        return [List]
    else:
        permutations = []
        for i in range(len(List)):
            rest = List[:i] + List[i + 1:]
            for j in permutation(rest):
                permutations.append([List[i]] + j)
        return permutations


list_1 = int(input("Введите стартовое число: "))
list_2 = int(input("Введите конечное число: "))
list = [x for x in range(list_1, list_2 + 1)]
permutations = permutation(list)
print("Все перестановки", permutations)
