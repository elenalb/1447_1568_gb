# конструкция yield

generator = (param ** 2 for param in range(3))

for param in generator:
    print(param)

# print(next(generator))


def my_generator():
    for el in (1, 2, 3):
        yield el


g = my_generator()
print(g)

for param in g:
    print(param)

# print(next(g))
