# Сформировать список из N членов последовательности. Для N = 5: 1, -3, 9, -27, 81 и т.д.

import random

def generate_random_numbers(n):
    return random.sample(range(100), int(n))

n = input("Введите N количество элементов списка: ")
random_numbers = generate_random_numbers(n)

print(random_numbers)

# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1. Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

def generate_dict_numbers(n):
    numbers_dict = {}
    for i in range(n):
        numbers_dict[i + 1] = 3 * (i + 1) + 1
    return numbers_dict

n = int(input("Введите N количество элементов словаря: "))
random_dict = generate_dict_numbers(n)

print(random_dict)

# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

str1 = input("Введите 1-ую строку: ")
str2 = input("Введите 2-ую строку: ")
str_entries_count = str1.count(str2)

print(f"Строка '{str2}' входит в строку '{str1}' {str_entries_count} раз")

# Подсчитать сумму цифр в вещественном числе.

def sum_float_number(number):
    sum_number = 0
    cnt_digit = len(number)
    for i in range(cnt_digit):
        if number[i] != '.' and number[i] != ',':
            sum_number += int(number[i])
    return sum_number

number = input("Введите вещественное число: ")
sum_float_number = sum_float_number(number)

print(f"Сумма цифр в числе {number} = {sum_float_number}")

# Написать программу получающую набор произведений чисел от 1 до N. Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]

def factorial_list(n):
    factorial_list = []
    for i in range(1, n + 1):
        if factorial_list:
            factorial_list.append(i * factorial_list[-1])
        else:
            factorial_list.append(1)
    return factorial_list

n = int(input("Введите N: "))
factorial_list = factorial_list(n)

print(f"Полученный набор: {factorial_list}")