# Вычислить число c заданной точностью d

# Пример: - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from math import pi

d = input('Задайте требуюмую точность для числа Пи (в формате: 0.00....1): ')
d = len(str(d).split('.')[1])
print(f'Число Пи с точностью {d} знака(знаков) после запятой: {round(pi, d)}')