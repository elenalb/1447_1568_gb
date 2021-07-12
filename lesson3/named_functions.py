# функции


def my_sum(arg1, arg2):
    return arg1 + arg2


print(my_sum(1, 2))
print(my_sum('hello, ', 'world'))


def ext_func(var1):
    def int_func(var2):
        return var1 + var2
    return int_func


f_obj = ext_func(300)
print(type(f_obj))
print(f_obj(20))


def my_func():
    pass  # оператор заглушка


print(my_func())


# return со значением
def s_calc():
    r_val = float(input("Введите радиус: "))
    h_val = float(input("Введите высоту: "))
    # площадь боковой поверхности
    s_side = 2 * 3.14 * r_val * h_val
    # площадь основания цилиндра
    s_circle = 3.14 * r_val ** 2
    # площадь полной поверхности
    s_full = s_side + 2 * s_circle
    return s_full


# s_val = s_calc()
# print(s_val)
#
# print(s_calc())


# return без значения
def s_calc_1():
    try:
        r_val = float(input("Введите радиус: "))
        h_val = float(input("Введите высоту: "))
    except ValueError:
        print("Вы ввели не числа!")
        return
    # площадь боковой поверхности
    s_side = 2 * 3.14 * r_val * h_val
    # площадь основания цилиндра
    s_circle = 3.14 * r_val ** 2
    # площадь полной поверхности
    s_full = s_side + 2 * s_circle
    return s_full, s_circle


s_val, s_circle = s_calc_1()
print(s_val, s_circle)
