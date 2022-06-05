#Написать программу вычисления арифметического выражения заданного строкой. Используются операции +,-,/,*. приоритет операций стандартный. Функцию eval не использовать!
#Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;


# Словарь операторов и их выполняющих функций с указанием приоритетов операций
OPERATORS = {
    '+': (1, lambda x, y: x + y), 
    '-': (1, lambda x, y: x - y),
    '*': (2, lambda x, y: x * y), 
    '/': (2, lambda x, y: x / y)
}

# Вычисляем мат. выражение в польской нотации. 
def calc(polish):
    stack = []
    for token in polish:
        if token in OPERATORS:  # если приходящий элемент - оператор,
            y, x = stack.pop(), stack.pop()  # забираем 2 числа из стека
            stack.append(OPERATORS[token][1](x, y)) # вычисляем оператор, результат возвращаем в стек
        else:
            stack.append(token)
    return stack[0] # результат вычисления - единственный элемент в стеке

# Сортируем операции в польской нотации по приоритету.
def sort_polish(infix):
    postfix = []
    stack = []
    for token in infix:
        if token in OPERATORS:
            while stack and OPERATORS[token][0] <= OPERATORS[stack[-1]][0]:
                postfix.append(stack.pop())
            stack.append(token)
        else:
            postfix.append(token)
    while stack:
        postfix.append(stack.pop())
    return postfix

# Паосим выражение в польскую нотацию.
def parse_infix(math_expression):
    polish = []
    number = ''
    for s in math_expression:
        if s.isdigit(): # если символ - цифра, то собираем число
            number += s  
        else: # если символ не цифра, то выдаём собранное число и начинаем собирать заново
            polish.append(float(number)) 
            number = ''
        if s in OPERATORS: # если символ - оператор, то выдаём как есть
            polish.append(s)
    if number:  # если в конце строки есть число, выдаём его
        polish.append(float(number)) 
    return polish 

# Вычисляет мат. выражение с помощью польской нотации.
def calc_math_expression(math_expression):
    polish_infix = parse_infix(math_expression)
    polish = sort_polish(polish_infix)
    return calc(polish)

math_expression = '2+2*2-4'
res = calc_math_expression(math_expression)
print(res)