import random

n = input('Введите целое число N (больше 0): ')

try:
    n = int(n)
    if n < 1: print('Вы ввели число меньше 1')
    else: 
        my_list = [random.uniform(1,10) for i in range(n)]
        print('Сгенерированный список из N элементов: ', my_list)
        
        my_list2 = [] 
        j = 0
        while j < n:
            my_list2.append(my_list[j]-int(my_list[j]))
            j = j + 1
        print('Разность между MAX и MIN дробной частью: ', max(my_list2)-min(my_list2))
except ValueError:
    print ('Вы ввели не целое число')