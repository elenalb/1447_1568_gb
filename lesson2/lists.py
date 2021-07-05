# списки

print(list("строка"))
my_list = [1, 2, True, "string"]

my_list.append([1, 2])  # добавляет элемент в конец
print(my_list)
my_list.extend([3, 4])
print(my_list)
my_list.insert(0, False)
print(my_list)
my_list.remove(False)
print(my_list)
my_list.pop(1)
print(my_list)
print(my_list.index('string'))  # получаем индекс первого вхождения элемента
# в качестве аргумента - конкретный элемент
print(my_list.count('string'))  # получаем количество элементов списка с конкретным значением
# в качестве аргумента - конкретный элемент
print([1, 1, 1, 2, 3, 4, 5, 4].count(4))
# 1 2 3
# 2 3 4
# 3 4 5
matrix = [[1, 2, 3],
          [2, 3, 4],
          [3, 4, 5]]
my_list.reverse()


print(my_list)
new_list = my_list.copy()
print(new_list)
new_list.clear()
print(new_list)

list1 = [1, 2, 3]
list2 = list1
print(list1)
print(list2)
print(id(list1) == id(list2))
print(list1 is list2)
list1.remove(1)
print(list2)
list2 = list1.copy()
print(id(list1) == id(list2))
print(list1 is list2)  # проверка тождественности

test_list = [1, 2, 3]
test_list2 = [1, 2]
all_elements_in = False
for element in test_list2:
    if element not in test_list:
        all_elements_in = False
    else:
        all_elements_in = True
print(all_elements_in)
# print(list1)
# print(1 in test_list or 2 in test_list)

# print((3 or 4) in test_list)  # проверка вхождения
# print((4 or 3) in test_list)  # проверка вхождения

# print((3 and 4) in test_list)  # проверка вхождения
# print((4 and 3) in test_list)  # проверка вхождения

