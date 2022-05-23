# Задать список из n чисел последовательности (1+1/n)**n и вывести на экран их сумму

from datetime import datetime
from time import time


def generate_list(n):
    list_numbers = []
    for i in range(1, n + 1):
        list_numbers.append((1+1/i)**i)
    return list_numbers

n = int(input("Введите N количество элементов списка: "))
lst = generate_list(n)
sum_numbers = sum(lst)

print(lst)
print(sum_numbers)