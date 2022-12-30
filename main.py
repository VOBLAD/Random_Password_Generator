import random
from art import *


tprint("Random Password", font="bulbehead")

chars = '+-/!&$#@?abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

number = int(input('Количество паролей:'))
lenght = int(input('Количество символов:'))


for x in range(number):
    password = ''
    for i in range(lenght):
        password += random.choice(chars)
    print(password)

    file = open('password.txt', 'a')
    file.write('\n' + password)
    file.close()
