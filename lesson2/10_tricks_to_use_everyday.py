# Десятка лучших трюков в Python

# объединеие списков без цикла
my_list = [[1, 2, 3], [2, 3], [40, 50, 100, 2]]
new_list = sum(my_list, [])
print(new_list)

# поиск уникальных элементов в списке
print(list(set(new_list)))

# обмен значениями через кортежи
var_1, var_2 = 20, 30
print(var_1, var_2)
var_1, var_2 = var_2, var_1
print(var_1, var_2)

# вывод значения несуществующего ключа в словаре
my_dict = {1: 'one', 2: 'two'}
print(my_dict.get(3))

# поиск самых часто встречающихся элементов списка
print(max(set(new_list), key=new_list.count))

# распаковка последовательностей при неизвестном количестве элементов
# оператор *

*el_1, el_2, el_3 = new_list
print(el_1, el_2, el_3)
el_1, el_2, el_3, *el_4 = new_list
print(el_1, el_2, el_3, el_4)

# вывод print() без перевода строки
for el in "string":
    print(el, end='')

# сортировка словаря по значениям
lang_dict = {'python': 1991, 'java': 1995, 'c++': 1985}
print(sorted(lang_dict))
print(sorted(lang_dict, key=lang_dict.get))

# нумерованные списки
for ind, el in enumerate([1, 2, 3]):
    print(ind + 1, el)

# транспонирование матрицы
old_matrix = [(1, 2, 3),
              (4, 5, 6)]
# 1 4
# 2 5
# 3 6
new_matrix = zip(*old_matrix)
print(list(new_matrix))
