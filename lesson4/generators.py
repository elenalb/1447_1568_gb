# генераторы списков

my_list = [1, 2, 3]
new_list_for_in = []
for element in my_list:
    new_list_for_in.append(element ** 2)
print(new_list_for_in)

new_list = [element ** 2 for element in my_list]
print(new_list)

lines = [line.strip() for line in open("my_module.py", encoding="UTF-8")]
print(lines)

odd_numbers = [element for element in my_list if element % 2 != 0]
print(odd_numbers)

str_1 = "abc"
str_2 = "d"
str_3 = "efg"

sets = [i + j + k for i in str_1 for j in str_2 for k in str_3]
print(sets)

my_tuple = (1, 2, 3)
new_tuple = (element ** 2 for element in my_tuple)

print(new_tuple)
for i in new_tuple:
    print(i)


# генераторы словарей и множеств
new_set = {element ** 2 for element in my_list}
print(new_set)

new_dict = {el: el ** 2 for el in my_list}
print(new_dict)
