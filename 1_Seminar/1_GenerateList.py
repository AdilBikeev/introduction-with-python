# Сформировать список из N членов последовательности. Для N = 5: 1, -3, 9, -27, 81 и т.д.

import random

def generate_list(n):
    list_numbers = []
    for i in range(0, n):
        list_numbers.append((-3)**i)
    return list_numbers

n = int(input("Введите N количество элементов списка: "))
random_numbers = generate_list(n)

print(random_numbers)