n = input('Введите целое число N (больше 0): ')

try:
    n = int(n)
    if n < 1: print('Вы ввели число меньше 1')
    else: 
        print('Для N = ', n, ': ', end='')
        result =[]
        for i in range(1,n+1):
            result.append([i, round((1 + 1/i)**i)])
        print(dict(result))
except ValueError:
    print ('Вы ввели не целое число')