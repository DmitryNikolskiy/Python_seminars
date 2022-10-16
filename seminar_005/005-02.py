# Дан список чисел. Создайте список, в который попадают числа, составляющие возрастающую последовательность. Порядок элементов менять нельзя
#

def nextmax(f_list):
    max = f_list[0]
    res = [f_list[0]]
    for i in range(len(f_list)):
        if f_list[i] > max:
            max = f_list[i]
            res.append(max)
    if len(res) == 1:                          # условие если сначала максимальное и оно одно
        res = nextmax(f_list[1:])              # убираем и считаем дальше
    return res

my_list = [11, 1, 5, 4, 3, 4, 6, 1, 7]
print(my_list)
print(nextmax(my_list))
