#2.	Создать и заполнить файл случайными целыми значениями. Выполнить сортировку содержимого файла по возрастанию. 

import random


def read_nums_from_file(file_name):
    nums_file = open(file_name, 'r')
    nums_input = [int(num) for num in nums_file.read().split()]
    nums_file.close()
    return nums_input

def write_nums_in_file(file_name, nums):
    nums_file = open(file_name, 'w')
    nums_file.write(nums)
    nums_file.close()

def generate_random_numbers(n):
    return random.sample(range(10), int(n))

def convert_nums_to_str(nums):
    nums_str = ' '.join(str(x) for x in nums)
    return nums_str

def fill_file_random_numbers(file_name, n):
    nums = generate_random_numbers(n)
    print("[DEBUG] сгенерированный список: ", nums)
    nums_str = convert_nums_to_str(nums)
    write_nums_in_file(file_name, nums_str)

def sort_numbers_from_file(file_name):
    nums = read_nums_from_file(file_name)
    nums.sort()
    nums_str = convert_nums_to_str(nums)
    write_nums_in_file(file_name, nums_str)

n = int(input("Введите N количество элементов списка: "))
fill_file_random_numbers('nums_random.txt', n)
sort_numbers_from_file('nums_random.txt')