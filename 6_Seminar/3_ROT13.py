# ROT13 - это простой шифр подстановки букв, который заменяет букву буквой, которая идет через 13 букв после нее в алфавите. ROT13 является примером шифра Цезаря.
# Создайте функцию, которая принимает строку и возвращает строку, зашифрованную с помощью Rot13 . Если в строку включены числа или специальные символы, они должны быть возвращены как есть. Также создайте функцию, которая расшифровывает эту строку обратно (некий начальный аналог шифрования сообщений). 
# Не использовать функцию encode.

def rot13(text, decode=False):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for i in text:
        if i in alphabet:
            if decode:
                result += alphabet[(alphabet.index(i) - 13) % 26]
            else:
                result += alphabet[(alphabet.index(i) + 13) % 26]
        else:
            result += i
    return result

input_text = "abcdefghijklmnopqrstuvwxyz"
print("input_text=", input_text)
encode_text = rot13(input_text)
print("encode_text=", encode_text)
decode_text = rot13(encode_text, decode=True)
print("decode_text=", decode_text)