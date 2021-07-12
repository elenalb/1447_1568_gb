# аргументы функций


# позиционные аргументы
def first_func(var_1, var_2, var_3):
    return var_1 + var_2 + var_3


print(first_func(1, 2, 3))


# именованные аргументы
def second_func(var_1, var_2, var_3):
    print(f"var_1 = {var_1}, var_3 = {var_3}, var_2 = {var_2}")


second_func(var_2=1, var_1=10, var_3=4)


# необязательные аргументы -- var_3
def third_func(var_1, var_2, var_3=10):
    return var_1 + var_2 + var_3


print(third_func(1, 2))


# мы можем передавать в функцию неопределенное количество аргументов!
def my_func(*args):
    return args


print(my_func(1, 2, True, 'var1'))


def my_kwarg_func(**kwargs):
    return kwargs


print(my_kwarg_func(var_1=1, var_2=True, var_3='hello'))
