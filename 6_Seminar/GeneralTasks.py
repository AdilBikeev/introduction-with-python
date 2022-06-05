#Написать программу вычисления арифметического выражения заданного строкой. Используются операции +,-,/,*. приоритет операций стандартный. Функцию eval не использовать!
#Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;


# Словарь операторов и их выполняющих функций с указанием приоритетов операций
OPERATORS = {
    '+': (1, lambda x, y: x + y), 
    '-': (1, lambda x, y: x - y),
    '*': (2, lambda x, y: x * y), 
    '/': (2, lambda x, y: x / y)
}

# Вычисляем мат. выражение в польской нотации. 
def calc(polish):
    stack = []
    for token in polish:
        if token in OPERATORS:  # если приходящий элемент - оператор,
            y, x = stack.pop(), stack.pop()  # забираем 2 числа из стека
            stack.append(OPERATORS[token][1](x, y)) # вычисляем оператор, результат возвращаем в стек
        else:
            stack.append(token)
    return stack[0] # результат вычисления - единственный элемент в стеке

# Сортируем операции в польской нотации по приоритету.
def sort_polish(infix):
    postfix = []
    stack = []
    for token in infix:
        if token in OPERATORS:
            while stack and OPERATORS[token][0] <= OPERATORS[stack[-1]][0]:
                postfix.append(stack.pop())
            stack.append(token)
        else:
            postfix.append(token)
    while stack:
        postfix.append(stack.pop())
    return postfix

# Паосим выражение в польскую нотацию.
def parse_infix(math_expression):
    polish = []
    number = ''
    for s in math_expression:
        if s.isdigit(): # если символ - цифра, то собираем число
            number += s  
        else: # если символ не цифра, то выдаём собранное число и начинаем собирать заново
            polish.append(float(number)) 
            number = ''
        if s in OPERATORS: # если символ - оператор, то выдаём как есть
            polish.append(s)
    if number:  # если в конце строки есть число, выдаём его
        polish.append(float(number)) 
    return polish 

# Вычисляет мат. выражение с помощью польской нотации.
def calc_math_expression(math_expression):
    polish_infix = parse_infix(math_expression)
    polish = sort_polish(polish_infix)
    return calc(polish)

math_expression = '2+2*2-4'
res = calc_math_expression(math_expression)
print(res)














# Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных файлах (в одном файлике отрывок из какой-то книги, а втором файлике — сжатая версия этого текста). 

def rle_encode(data):
    encoded = []
    count = 1
    for i in range(len(data)):
        if i == len(data) - 1: # Если последний символ
            encoded.append(str(count))
            encoded.append(data[i])
        elif data[i] == data[i + 1]: # Если символы повторяются
            count += 1
        else: # Если символы не повторяются - сжимаем ААА -> 3A
            encoded.append(str(count))
            encoded.append(data[i])
            count = 1
    return ''.join(encoded)

def rle_decode(data):
    decoded = []
    number = 0
    for i in range(len(data)):
        if data[i].isdigit():
            number = number * 10 + int(data[i])
        else:
            decoded.append(data[i] * number)
            number = 0
    return ''.join(decoded)

def read_text_from_file(file_name):
    file = open(file_name, 'r')
    data = file.read()
    file.close()
    return data

def write_text_in_file(file_name, text):
    file = open(file_name, 'w')
    file.write(text)
    file.close()

input_text = read_text_from_file('input_text_rle.txt')
output_text = rle_encode(input_text)
print("Исходный текст: ", input_text)
print("Кодированный текст: ", output_text)
write_text_in_file('output_text_rle.txt', output_text)
print("Раскодированный текст: ", rle_decode(output_text))















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