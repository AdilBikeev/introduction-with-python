# Определить, присутствует ли в заданном списке строк, некоторое число

# def get_hash_code(a):
#     a = str(a)
#     h = 0
#     for i in range(len(a)):
#         h = (31 * h + ord(a[i])) % 100000
#     return h

# def generate_random_numbers(n):
#     lst = []
#     for i in range(n):
#         lst.append(get_hash_code(str(i)))
#     return lst

def number_contains_in_text(text, number):
    for str in text:
        if number_contains_in_str(str, number):
            print("[DEBUG]: Число присутствует в строке: " + str)
            return True
    return False

def number_contains_in_str(str, number):
    if str.find(number) != -1:
        return True
    return False
    # words = str.split(" ")
    # #print("[DEBUG]: ", words)
    # for word in words:
    #     if word == number:
    #         return True
    # return False

number = input("Введите искомое число: ")
#nubmers_list = generate_random_numbers(5)
text = ["Привет 1", "24 настроение", "настрое7ние", "5настроение", "настроение6"]
print(f"Исходный список: {text}")
print(f"Искомое число {number} присутствует в списке {number_contains_in_text(text, number)}")


