import random

def candy_quantity(player):
    x = int(input(f'Игрок {player}, сколько вы возьмете конфет (от 1 до 28)? '))
    while x < 1 or x > 28:
        x = int(input(f'Игрок {player}, соблюдайте правила игры!'))
    return x


def message(player, k, val):
    print(f'Игрок {player} взял {k} конфет(ы). На столе осталось {val} конфет(ы).')


print('Условие задачи: \nНа столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. \nПервый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. \nВсе конфеты оппонента достаются сделавшему последний ход. \nСколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?')

first_player = input('Первый игрок: ')
second_player = input('Второй игрок: ')
value = int(input('Начальное количество конфет на столе: '))
order = random.randint(0,2)
if order:
    print(f'По жеребьевке первым ходит игрок: {first_player}')
else:
    print(f'По жеребьевке первым ходит игрок: {second_player}')

count1 = 0 
count2 = 0

while value > 28:
    if order:
        i = candy_quantity(first_player)
        count1 += i
        value -= i
        order = False
        message(first_player, i, value)
    else:
        j = candy_quantity(second_player)
        count2 += j
        value -= j
        order = True
        message(second_player, j, value)

if order:
    print(f'Победил игрок: {first_player}')
else:
    print(f'Победил игрок: {second_player}')