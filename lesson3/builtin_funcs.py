# встроенные функции

print(ord("a"))
print(chr(98))
print(len([1, 2, 3]))

print(abs(-10))
print(round(2.32442342, 3))
print(divmod(5, 2))
print(pow(2, 4))
list_1 = [1, 2, 3, 4, 5]
print(max(list_1))
print(min(list_1))
print(sum(list_1))

# функция range()
print(list(range(7)))  # [0, 7)
print(list(range(1, 10)))  # [1, 10)
print(list(range(2, 13, 2)))  # [2, 13)
print(list(range(1, -5, -1)))


for el in range(1, 10, 2):
    res = el / 2
    print(f"Результат деления {el} на 2 равен {res}")


print(range.__doc__)
