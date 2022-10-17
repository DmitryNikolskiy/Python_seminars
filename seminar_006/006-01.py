# напишите программу вычисления арифмитического выражения заданного строкой

my_text = '1-2*3*2-5+8/2'
# my_list = eval(my_text)              # не рекомендуемые функции
# exec(f'print({my_text})')            # не рекомендуемые функции


my_list = list(my_text)    
print(my_list)

i = 1

while '*' in my_list or '/' in my_list:
    if my_list[i] == '*':
        my_list[i-1] = int(my_list[i-1]) * int(my_list[i+1])
        del my_list[i+1]
        del my_list[i]
    elif my_list[i] == '/':
        my_list[i-1] = int(my_list[i-1]) / int(my_list[i+1])
        del my_list[i+1]
        del my_list[i]
    else: i += 1

print(my_list)

i = 1

while '+' in my_list or '-' in my_list:
    if my_list[i] == '+':
        my_list[i-1] = int(my_list[i-1]) + int(my_list[i+1])
        del my_list[i+1]
        del my_list[i]
    elif my_list[i] == '-':
        my_list[i-1] = int(my_list[i-1]) - int(my_list[i+1])
        del my_list[i+1]
        del my_list[i]
    else: i += 1

print(my_list)