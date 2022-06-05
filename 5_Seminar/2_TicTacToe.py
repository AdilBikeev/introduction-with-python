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