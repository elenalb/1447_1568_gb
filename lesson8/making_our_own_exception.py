# создание собственных исключений

try:
    res = 100 / 0
except ZeroDivisionError:
    print("На ноль делить нельзя!")
else:
    print(f"Все хорошо. Результат: {res}")
finally:
    print("Программа завершена")


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


input_data = input("Введите положительное число: ")

try:
    input_data = int(input_data)
    if input_data < 0:
        raise OwnError("Вы ввели отрицательное число!")
except ValueError:
    print("Вы ввели не число!")
except OwnError as err:
    print(err)
else:
    print(f"Все хорошо. Вы ввели число: {input_data}")
