def encryption(text, language, step):
    if language == "ru":
        n = 32
        last_char = ord("я")
    elif language == "en":
        n = 26
        last_char = ord("z")
    new_text =''
    for i in range(len(text)):
        if text[i].isalpha():
            new_char = ord(text[i].lower()) + int(step) % n
            if new_char > last_char:
                new_char -= n
            if text[i].isupper():
                new_text += chr(new_char).upper()
            else:
                new_text += chr(new_char)
        else:
            new_text += text[i]
    return new_text

def decryption(text, language, step):
    if language == "ru":
        n = 32
        first_char = ord("а")
    elif language == "en":
        n = 26
        first_char = ord("a")
    new_text =''
    for i in range(len(text)):
        if text[i].isalpha():
            new_char = ord(text[i].lower()) - int(step) % n
            if new_char < first_char:
                new_char += n
            if text[i].isupper():
                new_text += chr(new_char).upper()
            else:
                new_text += chr(new_char)
        else:
            new_text += text[i]
    return new_text

print("Вы хотите зашифровать или дешифровать текст?")
direction = input("Введите 1 для шифрования и 2 для дешифрования: ")
language =  input("На каком языке будет текст? (русский - ru / английский - en)  ").strip().lower()
step = input("С каким шагом будет сдвиг? ")

if direction == "1" and (language == "ru" or language == "en") and step.isdigit():
    print("Введите текст")
    text = input()
    print("Зашифрованный текст:")
    print(encryption(text, language, step))
elif direction == "2" and (language == "ru" or language == "en") and step.isdigit():
    print("Введите текст")
    text = input()
    print("Расшифрованный текст:")
    print(decryption(text, language, step))
else:
    print("Некорректно введены входные данные")
