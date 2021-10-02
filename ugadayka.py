from random import *

number = randint(99, 100)

print('Доброе пожаловать в числовую угадайку!')

def is_valid(num):
    if num.isdigit():
        num = int(num)
        if 1 <= num <= 100:
            return True
        else:
            return False
    else:
        return False

while True:
    response = input('Введите число от 1 до 100:')
    if not is_valid(response):
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue
    val = int(response)

    if val < number:
        print('Ваш число меньше загаданного, попробуйте еще разок')
    elif val > number:
        print('Ваше число больше загаданного, попробуйте еще разок')
    else:
        print('Вы угадали, поздравляем!')
        break
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')