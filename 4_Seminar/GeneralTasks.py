# 1.	Дан список чисел. Создать список, в который попадают числа, описываемые возрастающую последовательность. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д. Порядок элементов менять нельзя

def get_increasing_sequence(nums):
    res = []
    for i in range(len(nums)):
        if i == 0:
            res.append(nums[i])
        elif nums[i] > res[len(res) - 1]:
            res.append(nums[i])
    return res

nums = [int(num) for num in input("Введите последовательность через пробел: ").split()]
print("Возрастающая последовательность: ", get_increasing_sequence(nums))










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











# 3.	Вот вам файл с тысячей чисел. https://cloud.mail.ru/public/DQgN/LqoQzPEec
# Задача: найти триплеты и просто выводить их на экран. Триплетом называются три числа, которые в сумме дают 0. (решение будет долгим, ибо является демонстрационным при теме многопоточного программирования). 

TEST_CASE_FILE_NAME = "1Kints.txt"

def read_nums_from_file(file_name):
    nums_file = open(file_name, 'r')
    nums_input = [int(num) for num in nums_file.read().split()]
    nums_file.close()
    return nums_input

def get_triplett(nums):
    n = len(nums)
    triplett = []
    for i in range(n - 1):
        triplett_set = set()
        for j in range(i + 1, n):
            sum_pair = -(nums[i] + nums[j])
            if sum_pair in triplett_set:
                triplett.append((nums[i], nums[j], sum_pair))
            else:
                triplett_set.add(nums[j])
    return triplett

print(f"Триплеты из файла {TEST_CASE_FILE_NAME}:", get_triplett(read_nums_from_file(TEST_CASE_FILE_NAME)))