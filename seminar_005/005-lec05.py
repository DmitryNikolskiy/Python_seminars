# функция zip и enumerate

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4,5,8,9,3,7]
salary = [100000, 200000, 300000, 400000]

data = list(zip(users, ids, salary))
print(data)



users2 = ['user1', 'user2', 'user3', 'user4', 'user5']
data2 = list(enumerate(users))
print(data2)
