def rot13(message):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + 13)
                                     % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char) - ord('a') - 13)
                                     % 26 + ord('a'))
        else:
            encrypted_char = char
        encrypted_message += encrypted_char
    return encrypted_message


message = input("Введите фразу: ")
encrypted_message = rot13(message)
print("Зашифрованное сообщение:", encrypted_message)
