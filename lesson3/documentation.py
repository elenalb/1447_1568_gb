# Документирование кода функций
# PEP-257


def get_path():
    """Возвращает путь директории"""
    global my_path
    if my_path:
        return my_path


def my_func(arg_1=0, arg_2=1):
    """
    Возвращает сумму параметров
    :param arg_1: int, default = 0
    :param arg_2: int, default = 1
    :return: int
    """
    return arg_1 + arg_2


print(my_func.__doc__)
