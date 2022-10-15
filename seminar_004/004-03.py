# наименьшее общее кратное двух чисел

a, b = 100, 101
nok = max(a, b)
while not (nok % a ==0 and nok % b == 0):
    nok += max(a, b)
print(nok)