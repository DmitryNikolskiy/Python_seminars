import random

n = input('Введите целое число N (больше 0): ')

try:
    n = int(n)
    if n < 1: print('Вы ввели число меньше 1')
    else: 
        my_list = [random.randint(1,99) for i in range(n)]
        print('Сгенерированный список из N элементов: ', my_list)

        my_sum = 0
        j = 1
        while j < len(my_list):
            my_sum = my_sum + my_list[j]
            j=j+2 
        print('Сумма элементов на нечетных позициях: ', my_sum)   

except ValueError:
    print ('Вы ввели не целое число')