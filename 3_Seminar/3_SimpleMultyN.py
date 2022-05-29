#3	Составить список простых множителей натурального числа N

from cmath import sqrt
from math import floor


def get_prime_multipliers(num):
    simple_multy_lst = [1]
    max_division = num
    i = 2

    while pow(i, 2) <= max_division:
        while num % i == 0:
            simple_multy_lst.append(i)
            num //= i
        i += 1

    if num > 1:
        if num % i == 0:
            simple_multy_lst.append(i)
        else:
            simple_multy_lst.append(num)
    return simple_multy_lst

n = int(input("Введите число n: "))
print(get_prime_multipliers(n))