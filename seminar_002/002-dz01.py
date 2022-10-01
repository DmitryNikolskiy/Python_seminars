number = input('Введите число ')

try:
    number = float(number)
    sum = 0
    for i in str(number):
        if i != "-" and i !=".": sum = sum + int(i)
    print('Сумма чисел = ', sum)
except ValueError:
    print ('Вы ввели не вещественное число')