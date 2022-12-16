import random

def get_parameters_of_password():
    digits = "0123456789"
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    uppercace_lettrs = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    punctuation = "!#$%&*+-=?@^_"
    chars = ''
    terms = ''
    contain_digits = input('Включать ли цифры? (да / нет) ')
    if contain_digits == "да":
        chars += digits
        terms += 'д'
    else:
        terms += 'н'
    contain_uppercace = input('Включать ли прописные буквы? (да / нет) ')
    if contain_uppercace == "да":
        chars += uppercace_lettrs
        terms += 'д'
    else:
        terms += 'н'
    contain_lowercase = input('Включать ли строчные буквы? (да / нет) ')
    if contain_lowercase == "да":
        chars += lowercase_letters
        terms += 'д'
    else:
        terms += 'н'
    contain_punctuation = input('Включать ли символы? (да / нет) ')
    if contain_punctuation == "да":
        chars += punctuation
        terms += 'д'
    else:
        terms += 'н'
    exclude_ambiguous= input('Исключить неоднозначные символы (il1LoO0)? (да / нет) ')
    if exclude_ambiguous == "да":
        for c in 'il1LoO0':
            chars = chars.replace(c, '')
    return chars, terms

def generate_password(length, chars):
    password = ''
    for _ in range(length):
        password += random.choice(chars)
    return password

def check_password(password, terms):
    current_parameters = ["н","н","н","н"]
    for c in password:
        if c.isdigit():
            current_parameters[0] = 'д'
        elif c.isupper():
            current_parameters[1] = 'д'
        elif c.islower():
            current_parameters[2] = 'д'
        elif c in "!#$%&*+-=?@^_":
            current_parameters[3] = 'д'
    return ''.join(current_parameters) == terms
  

number_of_passwords = int(input('Сколько паролей требуется сгенерировать? '))
length_of_password = int(input('Какова требуемая длина пароля? '))
chars, terms = get_parameters_of_password()


for _ in range(number_of_passwords):
    while True:
        current_password = generate_password(length_of_password, chars)
        if check_password(current_password, terms) is True:
            print(current_password)
            break
    

