import random

n = input('Введите целое не отрицательное число:')

try:
    n = int(n)
    if n < 0: print('Вы ввели число меньше 0')
    elif n == 0:
        print('Число', n, 'в двоичной системе счисления равно', 0)
    else: 
        doub = str('')
        while n > 0:
            doub = str(n % 2) + doub 
            n = n // 2
        print('Число', n, 'в двоичной системе счисления равно', doub)
except ValueError:
    print ('Вы ввели не целое число')