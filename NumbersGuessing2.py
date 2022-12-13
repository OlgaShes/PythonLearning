import random

def is_valid(text, a, b):
    if text.isdigit():
        if a <= int(text) <= b:
            return True
    return False

def get_range():
    while True:
        n1 = input("Введите нижнюю границу чисел: ")
        n2 = input("Введите верхнюю границу чисел: ")
        if n1.isdigit() and n2.isdigit() and n1 <= n2:
            break
        print("Требуется ввести целые числа, при этом первое число должно быть меньше второго")
    return int(n1), int(n2)

def get_number(a, b):
    while True:
        guess = input(f'Введите число от {a} до {b}: ')
        if is_valid(guess, a, b) is False:
            print(f"Требовалось ввести целое число от {a} до {b}")
            continue
        else:
            return int(guess)

def game():
    num1, num2 = get_range()
    num = random.randint(num1, num2)
    count = 0
    while True:
        guess = get_number(num1,num2)
        count += 1
        if guess < num:
            print('Ваше число меньше загаданного, попробуйте еще раз')
        elif guess > num:
            print('Ваше число больше загаданного, попробуйте еще раз')
        else:
            print(f'Вы угадали c {count} раза, поздравляем!')
            break
        if count % 5 == 0:
            print("Хотите сдаться? (да / нет)")
            if input().lower() == 'да':
                break


print('Добро пожаловать в числовую угадайку')
print('Хотите сыграть? (да / нет)')
answer = input()
if answer.lower() == "да":
    while True:
        game()
        print('Спасибо, что играли в числовую угадайку. Хотите сыграть еще раз? (да / нет)')
        if input().lower() == "да":
            continue
        else:
            print('Тогда до встречи!')
            break
else:
    print('Ну нет так нет. До встречи!')



