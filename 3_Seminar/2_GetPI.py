# Вычислить число Пи c заданной точностью d
#	Пример: при d = 0.001,  c= 3.141. 

import math

def count_num_of_dec_places(num):
    i = 0
    while num % 10 != 1:
        num *= 10
        i+=1
    return i

def get_pi(accuracy):
    tochnost = count_num_of_dec_places(accuracy)
    pi_str = str(math.pi)
    return pi_str[:tochnost + 2]

d = float(input('Введите точность d: '))
print(f"PI={get_pi(d)}")
