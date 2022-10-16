# list comprehension
# быстрое создание списков

# список четных чисел в диапазоне от 1 до 100

'''
var1
list = []

for i in range(1, 101):
    if (i%2 == 0):
        list.append(i)
print(list)
'''

list = [i for i in range (1,101) if i % 2 == 0]
print(list)

# кортежи
list = [(i, i) for i in range (1,101) if i % 2 == 0]
print(list)

# функция + кортеж

def f(x):
    return x**3  

list2 = [(j, f(j)) for j in range (1,101) if j % 2 == 0]
print(list2)