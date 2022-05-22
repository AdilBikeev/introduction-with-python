# Реализовать алгоритм перемешивания списка
from math import floor
import random

def custom_shuffle(lst, n):
    for i in reversed(range(1, n)):
        j = floor(random.random() * (i + 1))
        lst[i], lst[j] = lst[j], lst[i]
    return lst

def generate_random_numbers(n):
    return random.sample(range(100), int(n))

n = int(input("Введите N количество элементов списка: "))
random_numbers = generate_random_numbers(n)
print(f"Сгенерированный список случайных чисел: {random_numbers}")
print(f"Перемешанный список: {custom_shuffle(random_numbers, n)}")
