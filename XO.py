import random
from time import sleep

def print_field(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if 0 < j < n - 1 and i != 0:
                print(' ' + str(matrix[i][j]).ljust(3), end='|')
            else:
                print(' ' + str(matrix[i][j]).ljust(3), end=' ')
        if i == 0 or i == n - 1:
            print()
            print()
        else:
            print()
            print('     ', '----' * (n-1))

def make_players_step(field, x_or_o):
    n = len(field)
    while True:
        print(f'Куда хотите поставить {x_or_o}? (ряд колонка): ')
        step = [int(c) for c in input().split(' ')]
        if 0 < step[0] < n and 0 < step[1] < n:
            if field[step[0]][step[1]] == ' ':
                field[step[0]][step[1]] = x_or_o
                return field
            else:
                print('Данное поле уже занято.')
        else:
            print('Введено неверное значение. Введите номер ряда и номер колонки через пробел.')

def make_bot_step(field, x_or_o):
    steps = list(range(0, len(field)))
    while True:
        step = [random.choice(steps) for i in range(2)]
        if field[step[0]][step[1]] == ' ':
            field[step[0]][step[1]] = x_or_o
            return field

def if_win(field, x_or_o):
    n = len(field)
    res1 = 0
    res2 = 0
    for i in range(1, n):
        res1 += 1 if field[i][i] == x_or_o else 0
        res2 += 1 if field[i][n - i] == x_or_o else 0
    if res1 == n - 1 or res2 == n - 1:
        return True
    for i in range(1, n):
        res1 = 0
        for j in range(1, n):
            res1 += 1 if field[i][j] == x_or_o else 0
        if res1 == n - 1:
            return True
    for j in range(1, n):
        res1 = 0
        for i in range(1, n):
            res1 += 1 if field[i][j] == x_or_o else 0
        if res1 == n - 1:
            return True
    return False

def play(field, p_step):
    print_field(field)
    if p_step == 'Х':
        b_step = 'O'
        turn = 0
        print('Вы ходите первым')
    else:
        b_step ='Х'
        turn = 1
        print('Бот ходит первым')
    count = 1
    while count <= (len(field) - 1)**2:
        if turn == 0:
            print('Твой ход:')
            field = make_players_step(field, p_step)
            count += 1
            print_field(field)
            if if_win(field, p_step) is True:
                print('Поздравляю, ты победил!')
                break
            turn = 1
        else:
            print('Ход бота:')
            field = make_bot_step(field, b_step)
            count += 1
            sleep(1)
            print_field(field)
            if if_win(field, b_step) is True:
                print('Бот победил!')
                break
            turn = 0
    else: print('К сожалению, ходы закончились, ничья')

print('Добро пожаловать в игру Крестики-Нолики')

print('Хотите сыграть? (да / нет)')
answer = input()
if answer.lower() == "да":
    while True:
        playing_field = [[0, 1, 2, 3],
                        [1, ' ', ' ', ' '],
                        [2, ' ', ' ', ' '],
                        [3, ' ', ' ', ' ']]
        print('Выхотите играть за Х или за О? (для выбора введите Х или О)')
        answer = input().lower()
        if answer == "х" or answer == "x":
            players_step = 'Х'
            play(playing_field, players_step)
        elif answer == "о" or answer == "o" or answer == "0":
            players_step = 'O'
            play(playing_field, players_step)
        else: 
            print('Введено неверное значение')
            continue
        print('Спасибо за игру! Хотите сыграть еще раз? (да / нет)')
        answer = input().lower()
        if answer == "да":
            continue
        elif answer == "нет":
            print('Тогда до встречи!')
            break
        else:
            print('Я тебя не совсем понял, но сочту за отказ. До встречи!')
            break
else:
    print('Ну нет так нет. До встречи!')