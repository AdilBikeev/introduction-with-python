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





# Вычислить число Пи c заданной точностью d
#	Пример: при d = 0.001,  c= 3.141. 

import math

def count_num_of_dec_places(num):
    i = 0
    while num % 10 != 1:
        num *= 10
        i+=1
    return i

def get_pi(accuracy):
    tochnost = count_num_of_dec_places(accuracy)
    pi_str = str(math.pi)
    return pi_str[:tochnost + 2]

d = float(input('Введите точность d: '))
print(f"PI={get_pi(d)}")





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





#Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
#	Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

def find_index_elem(elem, nums):
    for i in range(len(nums)):
        if nums[i] == elem:
            return i
    return -1

def get_unique_lst(nums):
    unique_lst = []
    for num in nums:
        if find_index_elem(num, unique_lst) == -1:
            unique_lst.append(num)
    return unique_lst

nums = [int(num) for num in input("Введите последовательность цифр через пробел: ").split()]
print('Последователньость из неповторяющихся элементов: ', get_unique_lst(nums))




#5.  Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа. 


def read_nums_from_file(file_name):
    nums_file = open(file_name, 'r')
    nums_input = [int(num) for num in nums_file.read().split()]
    nums_file.close()
    return nums_input

def write_nums_in_file(file_name, nums):
    nums_file = open(file_name, 'w')
    nums_file.write(nums)
    nums_file.close()

def remove_chet_num(nums):
    return [num for num in nums if num % 2 != 0]

def convert_nums_to_str(nums):
    nums_str = ' '.join(str(x) for x in nums)
    return nums_str

nums_input_file_name = u"nums_input.txt"
nums_output_file_name = u"nums_output.txt"
nums_input = read_nums_from_file(nums_input_file_name)

nums_output = convert_nums_to_str(remove_chet_num(nums_input))
write_nums_in_file(nums_output_file_name, nums_output)