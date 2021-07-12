import itertools

# функция count()
for el in itertools.count(5, 2):
    if el > 20:
        break
    else:
        print(el)


# функцию cycle()
c = 0
for el in itertools.cycle(["ABCDEF", "HIJKLMN"]):
    if c > 10:
        break
    print(el)
    c += 1

my_list = ["abc", "def", "ghi"]
cycle_iter = itertools.cycle(my_list)

print(next(cycle_iter))
print(next(cycle_iter))
print(next(cycle_iter))
print(next(cycle_iter))
print(next(cycle_iter))
print(next(cycle_iter))
print(next(cycle_iter))
print(next(cycle_iter))
print(next(cycle_iter))
print(next(cycle_iter))
print(next(cycle_iter))
print(next(cycle_iter))
print(next(cycle_iter))
