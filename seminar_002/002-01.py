import random

n = int(input('Введите целое число N (больше 0): '))
if n < 1: print('Вы ввели число меньше 1')
else: 
    for i in range(n-1):
        print(random.randint(1,99), end = ', ')
    print(random.randint(1,99))