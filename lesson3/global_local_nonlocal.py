# области видимости - локальная, глобальная, нелокальная
# локальная


def s_calc(r_val=3, h_val=4):
    # площадь боковой поверхности
    s_side = 2 * 3.14 * r_val * h_val
    # площадь основания цилиндра
    s_circle = 3.14 * r_val ** 2
    # площадь полной поверхности
    s_full = s_side + 2 * s_circle
    return s_full


s_val = s_calc()
print(s_val)


# нелокальная область видимости
def ext_func():
    my_var = 0

    def int_func():
        nonlocal my_var
        my_var += 1
        return my_var
    return int_func


func_obj = ext_func()
print(func_obj())
print(func_obj())
