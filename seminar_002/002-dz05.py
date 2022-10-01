import random

list = [1,56,4,32,64,21,10,3,5,53,11,98]
print ('Исходный список: ', list)

new_list = random.sample(list, len(list))
print ('Перемешанный список: ', new_list)