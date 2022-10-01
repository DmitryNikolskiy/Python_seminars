number = input('Введите число ')

try:
    number = float(number)
    summa = 0
    for i in str(number):
        if i != "-" and i !=".": summa = summa + int(i)
    print('Сумма чисел = ', summa)
except ValueError:
    print ('Вы ввели не вещественное число')