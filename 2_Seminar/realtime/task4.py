# Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел

def get_hash_code(a):
    a = str(a)
    h = 0
    for i in range(len(a)):
        h = (31 * h + ord(a[i])) % 100000
    return h

def generate_random_numbers(n):
    lst = []
    for i in range(n):
        lst.append(get_hash_code(str(i)))
    return lst

n = int(input("Введите N количество элементов списка: "))
lst = generate_random_numbers(n)
print(lst)