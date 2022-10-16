# функция map / filter

# my_list = [x for x in range(1,21)]
# print(my_list)

# my_list2 = list(map(lambda x:x+10, my_list))
# print(my_list2)


data = list(map(int, input().split()))
print(data)

res = filter(lambda x: not x % 2, data)
res = list(map(lambda x: (x,x**2), res))

print(res)