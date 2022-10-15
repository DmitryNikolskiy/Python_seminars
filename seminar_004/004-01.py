i = "1 5 6 7 5 2 9"
result = list(map(int, (i.split()))) # list - преобразование в список // map - итерирует по строке // split - разделяем строку
print(max(result), min(result))