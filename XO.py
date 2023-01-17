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
            print('   ', '-----' * (n-1))

def make_players_step(field, x_or_o):
    n = len(field)
    while True:
        print(f'Куда хотите поставить {x_or_o}? (ряд колонка): ')
        step = [int(c) for c in input().split()]
        if len(step) == 2 and 0 < step[0] < n and 0 < step[1] < n:
            if field[step[0]][step[1]] == ' ':
                field[step[0]][step[1]] = x_or_o
                return field
            else:
                print('Данное поле уже занято.')
        else:
            print('Введено неверное значение. Введите номер ряда и номер колонки через пробел.')
            continue

def make_bot_step(field, x_or_o):
    steps = list(range(0, len(field)))
    while True:
        step = [random.choice(steps) for i in range(2)]
        if field[step[0]][step[1]] == ' ':
            field[step[0]][step[1]] = x_or_o
            return field

def if_win(field, win_count, x_or_o):
    n = len(field)
    res1 = 0
    res2 = 0
    for i in range(1, n):
        res1 += 1 if field[i][i] == x_or_o else 0
        res2 += 1 if field[i][n - i] == x_or_o else 0
    if res1 == win_count or res2 == win_count:
        return True
    for i in range(1, n):
        res1 = 0
        for j in range(1, n):
            res1 += 1 if field[i][j] == x_or_o else 0
        if res1 == win_count:
            return True
    for j in range(1, n):
        res1 = 0
        for i in range(1, n):
            res1 += 1 if field[i][j] == x_or_o else 0
        if res1 == win_count:
            return True
    return False

def play(field, win_count, p_step):
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
            if if_win(field, win_count, p_step) is True:
                print('Поздравляю, ты победил!')
                break
            turn = 1
        else:
            print('Ход бота:')
            field = make_bot_step(field, b_step)
            count += 1
            sleep(1)
            print_field(field)
            if if_win(field, win_count, b_step) is True:
                print('Бот победил!')
                break
            turn = 0
    else: print('К сожалению, ходы закончились, ничья')

def get_field(num):
    field = [list(range(0, num + 1))]
    for i in range(1, num + 1):
        line = [i] + [' '] * num
        field.append(line)
    return field

def get_size():
    while True:
        num = input('Какой будет размер поля? (одной цифрой) -> ')
        if not num.isdigit():
            print('Надо ввести число')
            continue
        elif int(num) < 3:
            print('Это слишком мало')
            continue
        return int(num)

def get_count_for_win(size):
    while True:
        num = input('Сколько подряд должно быть для выигрыша? -> ')
        if not num.isdigit():
            print('Надо ввести число')
            continue
        elif int(num) < 3:
            print('Это слишком мало') 
            continue
        elif int(num) > size:
            print('Это больше, чем размер поля')
            continue
        return int(num)

def get_x_or_y():
    while True:
        print('Вы хотите играть за Х или за О? (для выбора введите Х или О)')
        answer = input().lower()
        if answer == "х" or answer == "x":
            return 'Х'
        elif answer == "о" or answer == "o" or answer == "0":
            return 'O'
        else: 
            print('Введено неверное значение')
            continue

print('Добро пожаловать в игру Крестики-Нолики')

print('Хотите сыграть? (да / нет)')
answer = input().lower().strip()
if answer == "да":
    while True:
        size = get_size()
        if size == 3:
            count_for_win = 3
        else:
            count_for_win = get_count_for_win(size)
        playing_field = get_field(size)
        players_step = get_x_or_y()
        play(playing_field, count_for_win, players_step)
        print('Спасибо за игру! Хотите сыграть еще раз? (да / нет)')
        answer = input().lower().strip()
        if answer == "да":
            continue
        elif answer == "нет":
            print('Тогда до встречи!')
            break
        else:
            print('Я тебя не совсем понял, но сочту за отказ. До встречи!')
            break
elif answer == "нет":
    print('Ну нет так нет. До встречи!')
else:
    print('Я тебя не совсем понял, но сочту за отказ. До встречи!')
