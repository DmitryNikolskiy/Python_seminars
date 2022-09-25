X = input('введите значение для переменной Х: ')
Y = input('введите значение для переменной Y: ')
Z = input('введите значение для переменной Z: ')

if not (X or Y or Z) == (not (X) and not (Y) and not (Z)): print(True)
else: print(False)