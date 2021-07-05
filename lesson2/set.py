# множества -- set()
set_1 = set("hello")
my_set_1 = {1, 11, 1, True, "string"}
print(set_1)
print(my_set_1)
set_1.add(1)
print(set_1)
set_1.remove("h")
print(set_1)
print(set_1.pop())  # удаляет первый элемент множества
print(set_1)
set_1.discard("h")

set_2 = frozenset("abrakadabra")
print(set_1)
print(set_1 == set_2)
print(set_2 - set_1)
print(set_1 | set_2)
set_3 = frozenset("abk")
print(set_3)
print(set_2)
print(set_3 in set_2)

