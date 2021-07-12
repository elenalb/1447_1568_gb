import functools

# функция reduce()


def my_func(prev_el, el):
    return prev_el + el


print(functools.reduce(my_func, [1, 2, 3, 4, 5]))
# [3, 3, 4, 5]
# [6, 4, 5]
# [10, 5]
# 15


# функция partial()
new_my_func = functools.partial(my_func, el=10)
print(new_my_func(100))
