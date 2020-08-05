a = input('Введите строку: ')
words = a.count(' ') + 1 # число слов
num = [int(i) for i in a if i.isdigit()]
print('Количество слов: ', words)
print('Количество цифр в тексте:', len(num))


