# кортежи - неизменяемая структура!

print(tuple("hello"))
my_tuple = (1, 2, True, "string")
my_list = [1, 2, True, "string"]
print(my_tuple)

print(my_tuple[0])
print(my_tuple.index("string"))
print(my_tuple.count("string"))

print(my_tuple.__sizeof__())
print(my_list.__sizeof__())
