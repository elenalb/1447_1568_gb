# анонимные функции - lambda функции, анонимные функции

my_lambda_func = lambda var_1, var_2: var_1 + var_2

print(my_lambda_func(1, 2))

print((lambda var_1, var_2: var_1 + var_2)(4, 5))


def named_func(arg):
    return arg ** 2


print(named_func(10))

lambda_func = lambda arg: arg ** 2

print(type(lambda_func))
print(lambda_func(10))
