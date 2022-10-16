# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.

def compressed(text):
    count = 1
    res = ''
    for i in range(len(text)-1):
        if text[i] == text[i+1]:
            count += 1
        else:
            res = res + str(count) + text[i]
            count = 1
    if count > 1 or (text[len(text)-2] != text[-1]):
        res = res + str(count) + text[-1]
    with open('C:/Users/Asus/Desktop/GeekBrains/Python/seminar_005/005-dz04_textfile_compressed.txt', "w") as f:
        f.write(res)
        f.close()    
    return res

def uncompressed(text):
    number = ''
    res = ''
    for i in range(len(text)):
        if not text[i].isalpha():
            number += text[i]
        else:
            res = res + text[i] * int(number)
            number = ''
    with open('C:/Users/Asus/Desktop/GeekBrains/Python/seminar_005/005-dz04_textfile_uncompressed.txt', "w") as f:
        f.write(res)
        f.close()   
    return res


with open('C:/Users/Asus/Desktop/GeekBrains/Python/seminar_005/005-dz04_textfile.txt', "r") as f:
    data = f.read()
    f.close()

print(f'Сжатие данных: {compressed(data)}')
print(f'Распакованные данные: {uncompressed(compressed(data))}')