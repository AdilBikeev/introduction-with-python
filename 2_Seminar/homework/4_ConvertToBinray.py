# Написать программу преобразования десятичного числа в двоичное

def convert_to_binary(number):
    result = ''
    while number > 0:
        result = str(number % 2) + result
        number = number // 2
    return result

number = int(input("Введите десятичное число: "))
print(f"Двоичное представление числа: {convert_to_binary(number)}")