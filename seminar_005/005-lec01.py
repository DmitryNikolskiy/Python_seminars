# def f(x):
#    return x**2

# g = f # присваиваем переменной ссылку на функцию
#print(f(2))
#print(type(f))  #просмотр типа функции

#print(g(4))

# def sum(x, y):
#   return x+y

#sum = lambda x, y: x+y
    
#def mylt(x, y):
#    return x*y
    
def calc(operation, a, b):
    print(operation(a, b))
#   return operation(a, b)


print(lambda x, y: x+y, 4, 5)