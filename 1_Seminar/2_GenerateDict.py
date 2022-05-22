# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1. Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

def generate_dict_numbers(n):
    numbers_dict = {}
    for i in range(1, n + 1):
        numbers_dict[i] = 3 * (i) + 1
    return numbers_dict

n = int(input("Введите N количество элементов словаря: "))
random_dict = generate_dict_numbers(n)

print(random_dict)