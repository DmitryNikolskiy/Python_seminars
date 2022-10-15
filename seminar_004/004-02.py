# a*x**2 + b*x + c = 0
a = -3
b = 8
c = 16
disc = b**2 - 4 * a * c  # находим дискриминант

if a == 0:
    x = -c / b
    print(x)
elif disc > 0:
    x1 = (-b - disc**0.5) / (2 * a)
    x2 = (-b + disc**0.5) / (2 * a)
    print(x1, x2)
elif not disc:  # disc = 0
    x = -b / (2 * a)
    print(x)
else: print('Нет вещественных корней')