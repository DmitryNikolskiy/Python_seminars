import random

n = input('Введите целое число N (больше 0): ')

try:
    n = int(n)
    if n < 1: print('Вы ввели число меньше 1')
    else: 
        my_list = [random.randint(1,10) for i in range(n)]
        print('Сгенерированный список из N элементов: ', my_list)

        my_list2 = [] 
        j = 0
        while j < n/2:
            my_list2.append(my_list[j]*my_list[n-1-j])
            j = j + 1
        print('Новый список: ', my_list2)
except ValueError:
    print ('Вы ввели не целое число')