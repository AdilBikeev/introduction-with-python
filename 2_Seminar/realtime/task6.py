# Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# пример:
# пример:
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1

def find_second_string_in_list(words, str):
    cnt_find = 0
    for i in range(len(words)):
        if words[i] == str:
            cnt_find += 1
            if cnt_find == 2:
                return i
    return -1
    
words = ["qwe", "asd", "zxc", "qwe", "ertqwe", "qwe"]
pivot = "qwe"
second_index = find_second_string_in_list(words, pivot)
print(f"Исходный список: {words}")
print(f"Искомая строка: {pivot}")
print(f"Позиция второго вхождения: {second_index}")