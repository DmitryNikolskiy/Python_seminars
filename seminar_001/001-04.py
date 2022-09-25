a = str(input('Введите дробь: '))
n = 0
for i in a:
    n += 1
    if i == "," or i == ".": print(a[n])