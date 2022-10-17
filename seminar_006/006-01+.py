# напишите программу вычисления арифмитического выражения заданного строкой

# my_list = eval(my_text)              # не рекомендуемые функции
# exec(f'print({my_text})')            # не рекомендуемые функции


def calc(my_list):

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
    return my_list

my_text = '1-2*3*(2*8-5)+8/2'
my_list_out = list(my_text)    


while '(' in my_list_out:
    bracket_left = my_list_out.index('(')
    bracket_right = my_list_out.index(')')
    my_list_out = my_list_out[:bracket_left] + calc(my_list_out[bracket_left + 1 : bracket_right]) + my_list_out[bracket_right+1:]

print(my_text + ' => ' + str(calc(my_list_out)[0]))