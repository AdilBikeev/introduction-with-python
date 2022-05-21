# Сформировать список из N членов последовательности. Для N = 5: 1, -3, 9, -27, 81 и т.д.

import random

def generate_random_numbers(n):
    return random.sample(range(100), int(n))

n = input("Введите N количество элементов списка: ")
random_numbers = generate_random_numbers(n)

print(random_numbers)