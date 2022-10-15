i = '1 5 6 7 5 2 9'
result = list(map(int, (i.split()))) # list - преобразование в список // map - функция итерирует по строке // split - разделяем строку
print(max(result), min(result))

num = '2 54 6  7 8  89 56 3'
my_list = [int(num) for num in num.split()]
print(max(my_list), min(my_list))