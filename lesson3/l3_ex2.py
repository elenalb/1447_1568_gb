"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""


def print_user_info(
        name='Ivan',
        surname='Ivanov',
        birth_year='1990',
        city='default_city',
        email='iivanov@gmail.com',
        tel_number='88005553535'):
    print(f"Имя: {name}, Фамилия: {surname}, год рождения: {birth_year}, город проживания: {city}, "
          f"e-mail: {email}, номер телефона: {tel_number}")


print_user_info(name="Lena")
