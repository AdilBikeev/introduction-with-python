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