X1 = int(input('Введите координату X первой точки: '))
Y1 = int(input('Введите координату Y первой точки: '))
X2 = int(input('Введите координату X второй точки: '))
Y2 = int(input('Введите координату Y второй точки: '))

from math import sqrt
print('Длина отрезка: ', sqrt((X2-X1) ** 2 + (Y2-Y1) ** 2))