# Напишите программу, удаляющую из текста все слова содержащие "абв", которое регистронезависимо. Используйте знания с последней лекции. Выполните ее в виде функции. 
# Пример: «абвгдеж рабав копыто фабв Абкн абрыволк аБволк»

def where(expression, col):
    return [x for x in col if expression(x)]

def filter_text_by_word(text, word):
    words = text.split()
    filtered_words = where(lambda w: w.find(word) == -1, words) 
    return ' '.join(w for w in filtered_words)

text = input("Введите исходный текст: ")
word_filter = input("Введите слово для фильтрации: ")
filtered_text = filter_text_by_word(text, word_filter)
print("Текст с отфильтрованными словами: ", filtered_text)

    





#Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её, причем чтобы сыграть в нее можно было в одиночку. 


    import os

def print_playing_field(playing_field):
    print("-" * 13)
    for i in range(3):
        print("|", playing_field[0+i*3], "|", playing_field[1+i*3], "|", playing_field[2+i*3], "|")
        print("-" * 13)

def next_step(player_token, playing_field):
    valid = False
    while not valid:
        player_answer = input("Выберите не занятую клетку для " + player_token+": ")
        player_answer = int(player_answer)
        if player_answer >= 1 and player_answer <= 9:
            if (str(playing_field[player_answer-1]) not in "XOХО0"):
                playing_field[player_answer-1] = player_token
                valid = True
            else:
                print("Данная клетка занята")
        else:
            print("К вводу доступны только не занятые клетки, содержащие цифры от 1 до 9")

def check_win(playing_field):
    winning_moves = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for win_comb in winning_moves:
        if playing_field[win_comb[0]] == playing_field[win_comb[1]] == playing_field[win_comb[2]]:
            return playing_field[win_comb[0]]
    return False

def start_game():
    clear = lambda: os.system('cls') # for linux -> clear
    playing_field = list(range(1,10)) # игровое поле
    round = 0 # номер раунда/хода
    win = False # флаг окончания игры
    while not win:
        print_playing_field(playing_field)
        if round % 2 == 0: # для чередования ходов проверяем на четность
            next_step("X", playing_field)
        else:
            next_step("O", playing_field)
        round += 1
        if round > 4: # как минимум после 3 ходов - должен появится победитель
            winner = check_win(playing_field)
            if winner:
                clear()
                print("Победил ", winner)
                win = True
                break
        if round == 9: # если до 9 раунда не выпала выигрышная комбинация - значит нитко не выиграл
            print("Ничья")
            break
        clear()
    print_playing_field(playing_field)

start_game()













# Вот вам текст:
# «Ну, вышел я, короче, из подъезда. В общем, короче говоря, шел я, кажется, в магазин. Ну,эээ, в общем, было лето, кажется. Как бы тепло. Солнечно, короче. Иду я, иду, в общем, по улице, а тут, короче, яма. Я, эээээ…. Упал в нее. И снова вышел, короче, из подъезда. Ясен пень, в магазин. В общем, лето на дворе, жарко, солнечно, птицы, короче, летают. Кстати, иду я по улице, иду, а тут, короче, яма. Ну, я в нее упал, в общем. Вышел из подъезда, короче. Лето на дворе, ясен пень. Птицы поют, короче, солнечно. В общем, в магазин мне надо. Что-то явно не так, короче. «Рекурсия», - подумал я. Ээээ...короче, в общем, пошел другой дорогой и не упал в эту… ээээ… яму. Хлеба купил».
# Отфильтруйте его, чтобы этот текст можно было нормально прочесть. Предусмотрите вариант, что мусорные слова могли быть написаны без использования запятых.

import re


def filter_text_by_regex(text, regex):
    return re.sub(regex, '', text, flags=re.IGNORECASE)

def filter_text_by_list(text, dict):
    for word in dict:
        text = filter_text_by_regex(text, word)
    return text

def replace_text_by_dict(text, dict):
    for key, value in dict.items():
        text = re.sub(key, value, text, flags=re.IGNORECASE)
    return text

def filter_text(text):
    word_filter = [
        "ну",
        "короче говоря",
        "короче",
        "в общем",
        "кажется",
        "кстати"
        r".э{2,}",
        r'\.{2,}',
        r".э{2,}",
        r'…',
    ]
    extra_symbols = [
        r' , ',
        #r', ',
        r' {2,}'
    ]
    map_replace = {
        r'\.,' : '. ',
        r',\.': ' ... ',
        r', \.': '.',
        r'«, ': '«'
    }
    text = filter_text_by_list(text, word_filter)
    text = filter_text_by_list(text, extra_symbols)
    text = replace_text_by_dict(text, map_replace)
    return text

input_text = """«Ну, вышел я, короче, из подъезда. В общем, короче говоря, шел я, кажется, в магазин. Ну,эээ, в общем, было лето, кажется. Как бы тепло. Солнечно, короче. Иду я, иду, в общем, по улице, а тут, короче, яма. Я, эээээ…. Упал в нее. И снова вышел, короче, из подъезда. Ясен пень, в магазин. В общем, лето на дворе, жарко, солнечно, птицы, короче, летают. Кстати, иду я по улице, иду, а тут, короче, яма. Ну, я в нее упал, в общем. Вышел из подъезда, короче. Лето на дворе, ясен пень. Птицы поют, короче, солнечно. В общем, в магазин мне надо. Что-то явно не так, короче. «Рекурсия», - подумал я. Ээээ...короче, в общем, пошел другой дорогой и не упал в эту… ээээ… яму. Хлеба купил»."""

filtered_text = filter_text(input_text)
print("Отфильтрованный текст: ", filtered_text)