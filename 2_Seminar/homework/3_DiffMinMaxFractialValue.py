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