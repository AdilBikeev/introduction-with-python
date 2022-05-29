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