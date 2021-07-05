# строка - str()

my_str = "строка"
# строка
# 012345
# -6 -5 -4 -3 -2 -1
print(my_str)
print(type(my_str))

# конкатенация
s_1 = "abc"
s_2 = "def"
print(s_1 + s_2)

# взятие элемента по индексу
print(my_str[3])
print(my_str[0])
print(my_str[-1])

# извлечение среза - var_name[s:f:step]
print(my_str[0:3])
print(my_str[0:5:2])
print(my_str[2:])
print(my_str[:4])
print(my_str[:])
print(my_str[1:-1])
print(my_str[::-1])

# механизмы реверса строк
# обратный срез !!
print(my_str[::-1])
# обратная итерация
for el in reversed(my_str):
    print(el, end='')
# реверс на месте
str_reversed = ''
symbols = list(my_str)
for el in range(len(my_str) // 2):
    tmp = symbols[el]
    symbols[el] = symbols[len(my_str) - el - 1]
    symbols[len(my_str) - el - 1] = tmp
str_reversed = ''.join(symbols)
print(str_reversed)

# методы строк
print(len(my_str))  # длина строки
print("hello this is     a           sentence".split())
print("hello, world".split(','))
# ['hello', 'world'] -> 'hello,world'
print(' HELLO '.join(['hello', 'world']))
print("hello this is a sentence".title())
print("hello this is a sentence".capitalize())
print("hello this is a sentence".upper())  # lower() - обратная операция
print("hello this is a sentence".count('is'))
print("hello this is a sentence".replace("is", "123"))
