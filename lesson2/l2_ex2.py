"""
Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами
0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

my_list = []
list_el = 0
el_count = 0
while list_el != 'stop':
    list_el = (input("Введите следующее значение списка (напишите stop для остановки ввода): "))
    if list_el != 'stop':
        my_list.append(list_el)

counter = len(my_list)
print(my_list)

for el in range(int(len(my_list) / 2)):
    my_list[el_count], my_list[el_count + 1] = my_list[el_count + 1], my_list[el_count]
    el_count += 2

print(my_list)
