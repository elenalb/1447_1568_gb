# оператор is - проверка тождественности

a = 20
b = 30

message = ("Переменные не идентичны", "Переменные идентичны")[a is b]
print(message)

# is != == !!!!!!
list1 = [1, 2, 3]
list2 = list1.copy()
message = ("Переменные не идентичны", "Переменные идентичны")[list1 is list2]
print(message)
message = ("Переменные не равны", "Переменные равны")[list1 == list2]
print(message)
