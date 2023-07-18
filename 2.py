def find_palindromic_substrings(string):
    palindromes = []

    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substring = string[i:j]

            if substring == substring[::-1]:
                palindromes.append(substring)

    return palindromes


input_string = "madam arora teaches malayalam"
result = find_palindromic_substrings(input_string)
print(result)
