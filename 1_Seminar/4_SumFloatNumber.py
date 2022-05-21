# Подсчитать сумму цифр в вещественном числе.

def sum_float_number(number):
    sum_number = 0
    cnt_digit = len(number)
    for i in range(cnt_digit):
        if number[i] != '.' and number[i] != ',':
            sum_number += int(number[i])
    return sum_number

number = input("Введите вещественное число: ")
sum_float_number = sum_float_number(number)

print(f"Сумма цифр в числе {number} = {sum_float_number}")