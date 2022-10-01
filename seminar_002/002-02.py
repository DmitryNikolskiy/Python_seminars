n = int(input('Введите целое число N (больше 0): '))
if n < 1: print('Вы ввели число меньше 1')
else: 
    print('Для N = ', n, ': ', end='')
    result =[]
    for i in range(1,n+1):
        result.append([i, 3*i+1])
    print(dict(result))