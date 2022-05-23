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