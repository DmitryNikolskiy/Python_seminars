# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k=int(input('Введите целое число - степень многочлена: '))
for i in range(3):
    result = ''
    for j in range (0, k+1):
        coef = random.randint(0,99)
        if not coef ==0:
            if j == 0:
                result = str(coef)
            elif j == 1:
                if not coef == 1:
                    result = str(coef) + '*x' + result
                else:
                    result = 'x' + result
            else:
                if not coef == 1:
                    result = str(coef) + '*x**' + str(j) + result
                else:
                    result = 'x**' + str(j) + result
            result = '+' + result
if result[0] == '+':
    result = result[1:]
print(result)