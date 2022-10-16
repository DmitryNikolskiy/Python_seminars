# напишите программу, удаляющую из текста все слова, содержащие абв

my_text = 'напишите програбвмму, удалабвяющую из текста всеабв словабв, сабводержащие абв'

my_text_list = list(filter(lambda x: 'абв' not in x, my_text.split()))
my_text2 = ' '.join(my_text_list)
print(my_text)
print(my_text2)