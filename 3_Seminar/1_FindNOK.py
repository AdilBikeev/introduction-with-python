# Найти НОК двух чисел

import math


def find_NOK(num1, num2):
    if num1 == 0 or num2 == 0:
        return 0

    num_max = max(num1, num2)
    num_min = min(num1, num2)

    if num_max % num_min == 0:
        return num_max

    for i in range(1, num_min):
        nok = num_max * i
        if nok % num_min == 0:
            return nok

    return num_min * num_max

[num1, num2] = [int(num) for num in input("Введите 2 числа через пробел: ").split()]
print(f'НОК={find_NOK(num1, num2)}')