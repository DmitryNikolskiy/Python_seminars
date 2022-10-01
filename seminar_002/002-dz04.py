n = input('Введите целое число N (больше 0): ')

try:
    n = int(n)
    if n < 1: print('Вы ввели число меньше 1')
    else: 
        sequence = list(range(-n, n+1))
        data = open("C://Users/Asus/Desktop/GeekBrains/Python/seminar_002/file.txt", 'r')
        multiple = 1
        for index in data:
            multiple = sequence[int(index)]*multiple
        data.close()
        print('Последовательность от -N до N: ', sequence')
        print('Произведение двух чисел на позициях из файла =', multiple)
except ValueError:
    print ('Вы ввели не целое число')