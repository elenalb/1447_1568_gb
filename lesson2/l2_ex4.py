"""
Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
"""
user_str = input('Введи строку: ')
my_list = user_str.split()
word_num = 0
for el in my_list:
    word_num += 1
    if len(el) < 10:
        print(f'{word_num}. {el}')
    else:
        print(f'{word_num}. {el[:10]}')

for ind, el in enumerate(my_list):
    if len(el) < 10:
        print(f'{ind + 1}. {el}')
    else:
        print(f'{ind + 1}. {el[:10]}')
