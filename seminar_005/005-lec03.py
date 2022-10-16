# считываем из файла строку со значениями и создаем список кортежей из четных чисел и их квадратов

# var 1

path = 'C:/Users/Asus/Desktop/GeekBrains/Python/seminar_005/file.txt'
f = open(path, 'r')
data = f.read() + ' '
f.close()

numbers = []

while data != '':
    space_pos = data.index(' ')
    numbers.append(int(data[:space_pos]))
    data = data[space_pos+1:]

    out = []
    for e in numbers:
        if not e % 2:
            out.append((e, e**2))
print(out)

# var 2

def select(f, col):
    return [f(x) for x in col]

def where (f, col):
    return [x for x in col if f(x)]

path = 'C:/Users/Asus/Desktop/GeekBrains/Python/seminar_005/file.txt'    # если просто из строки, а не из файла: numbers = '2 4 5 7 6 2 12 33 20 50 14 60 7 96 99'.split()
f = open(path, 'r')
data = f.read() + ' '
f.close()

numbers = []

while data != '':
    space_pos = data.index(' ')
    numbers.append(int(data[:space_pos]))
    data = data[space_pos+1:]

res = select(int, numbers)
res = where(lambda x: not x % 2, res)
res = select (lambda x: (x,x**2), res)

print(res)