from random import *

digits = '0123456789',
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz',
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
punctuation = '!#$%&*+-=?@^_.'
ambiguous = 'il1Lo0O'


def generate_password(length, chars):
    # global char
    print('Включать ли цифры? Y/N')
    if_digits = input()
    if if_digits == 'Y':
        chars = '{}{}'.format(chars, digits)
    print('Включать ли прописные буквы? Y/N')
    if_upper = input()
    if if_upper == 'Y':
        chars = '{}{}'.format(chars, uppercase_letters)
    print('Включать ли строчные буквы? Y/N')
    if_lower = input()
    if if_lower == 'Y':
        chars = '{}{}'.format(chars, lowercase_letters)
    print('Включать ли символы? Y/N')
    if_punct = input()
    if if_punct == 'Y':
        chars = '{}{}'.format(chars, punctuation)
    print('Исключать ли неоднозначные символы "il1Lo0O"? Y/N')
    if_amb = input()
    if if_amb == 'Y':
        for i in ambiguous:
            if i in chars:
                chars = chars.replace(i, '')
    print('Генерируем пароли!')

    for i in range(count_password + 1):
        print(*(sample(chars, length)), sep='')

char = ''

print('Сколько паролей нужно сгенерировать?')
count_password = int(input())
print('Сколько символов будет в пароле?')
length = int(input())

generate_password(length, char)