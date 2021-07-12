import random

print(random.randint(-100, 10))  # верхняя и нижняя границы включены в диапазон

print(random.randrange(10))  # верхняя граница в диапазон не включается!
print(random.randrange(10, 100))
print(random.randrange(10, 100, 10))

print(random.random())
print(random.random() * 10)  # меняем верхнюю границу
print(random.random() * (10 - 6) + 6)  # меняем и верхнюю и нижнюю границы

print(random.uniform(0, 10))

my_list = [1, 2, 3]
print(random.choice(my_list))
random.shuffle(my_list)
print(my_list)
