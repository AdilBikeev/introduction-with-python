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