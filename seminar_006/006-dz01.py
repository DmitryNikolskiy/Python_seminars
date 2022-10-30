#    Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#    Пример: 6782 -> 23

number = input('Введите положительное число ')

try:
    number = float(number)
    summa = sum(map(int, str(number).replace('.', '')))
    print('Сумма чисел = ', summa)
except ValueError:
    print ('Вы ввели не вещественное число')