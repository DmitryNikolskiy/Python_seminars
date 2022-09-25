n = int(input('Введите целое число N (больше 0): '))
if n < 1: print('Вы ввели число меньше 1')
else: 
    r = range(n-n*2, n)
    for i in r:
        print(i, end = ', ')
    print(n)