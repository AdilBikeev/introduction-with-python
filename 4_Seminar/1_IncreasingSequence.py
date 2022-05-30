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