# Найти сумму чисел списка стоящих на нечетной позиции

import random

def generate_random_numbers(n):
    return random.sample(range(10), n)

def sum_numbers_by_predicate(lst, predicate):
    sum = 0
    for i in range(len(lst)):
        if predicate(i):
            sum += lst[i]
    return sum

n = int(input("Введите N количество элементов списка: "))
random_numbers = generate_random_numbers(n)
print(f"Сгенерированный список случайных чисел: {random_numbers}")
print(f"Сумма чисел списка стоящих на нечетной позиции: {sum_numbers_by_predicate(random_numbers, lambda i: i % 2 != 0)}")








# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 

import math
import random

def generate_random_numbers(n):
    return random.sample(range(10), n)

def product_of_pairs_list(lst):
    product_pairs_list = []
    for i in range(math.ceil(len(lst) / 2)):
        product_pairs_list.append(lst[i] * lst[-i-1])
    return product_pairs_list

n = int(input("Введите N количество элементов списка: "))
random_numbers = generate_random_numbers(n)
print(f"Сгенерированный список случайных чисел: {random_numbers}")
print(f"Произведение пар чисел в списке: {product_of_pairs_list(random_numbers)}")










# В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. 
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19


import decimal
import random

def gen_random_decimal_lst(n):
    return [gen_random_decimal() for i in range(n)]

def gen_random_decimal():
    return decimal.Decimal('%d.%d' % (random.randint(0, 10),random.randint(0, 10)))

def remove_int_value(lst):
    return [item - int(item) for item in lst]

def diff_min_max_fractial_value(lst):
    fractial_list = remove_int_value(lst)
    print(f"[DEBUG] Список чисел без целой части: {fractial_list}")
    return max(fractial_list) - min(fractial_list)

n = int(input("Введите N количество элементов списка: "))
random_numbers = gen_random_decimal_lst(n)
print(f"Сгенерированный список случайных чисел: {random_numbers}")
print(f"Разница между максимальным и минимальным значением дробной части элементов: {diff_min_max_fractial_value(random_numbers)}")













# Написать программу преобразования десятичного числа в двоичное

def convert_to_binary(number):
    result = ''
    while number > 0:
        result = str(number % 2) + result
        number = number // 2
    return result

number = int(input("Введите десятичное число: "))
print(f"Двоичное представление числа: {convert_to_binary(number)}")