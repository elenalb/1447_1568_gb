"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма
чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный
символ, выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно
добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""


def inf_sum_func():
    result_sum = 0
    while True:
        input_list = input("Введите числа через пробел. Для выхода, напишите exit: ").split()
        try:
            for digit in input_list:
                result_sum += int(digit)
            print(f"Сумма введенных чисел равна {result_sum}")
        except ValueError:
            print(f"Выходим из программы! Конечная сумма: {result_sum}")
            return


inf_sum_func()
