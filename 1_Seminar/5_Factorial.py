# Написать программу получающую набор произведений чисел от 1 до N. Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]

def factorial_list(n):
    factorial_list = []
    for i in range(1, n + 1):
        if factorial_list:
            factorial_list.append(i * factorial_list[-1])
        else:
            factorial_list.append(1)
    return factorial_list

n = int(input("Введите N: "))
factorial_list = factorial_list(n)

print(f"Полученный набор: {factorial_list}")