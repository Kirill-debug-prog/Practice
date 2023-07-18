def permutation(l):
    if len(l) == 0:
        return [[]]
    elif len(l) == 1:
        return [l]
    else:
        permutations = []
        for i in range(len(l)):
            rest = l[:i] + l[i + 1:]
            for j in permutation(rest):
                permutations.append([l[i]] + j)
        return permutations


l_1 = int(input("Введите стартовое число: "))
l_2 = int(input("Введите конечное число: "))
l = [x for x in range(l_1, l_2 + 1)]
permutations = permutation(l)
print("Все перестановки", permutations)
