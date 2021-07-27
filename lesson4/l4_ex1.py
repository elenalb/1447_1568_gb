"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv

script_name, hours, pay_per_hour, bonus = argv


def calculate_salary(hours, pay_per_hour, bonus):
    return hours * pay_per_hour + bonus


salary = calculate_salary(int(hours), int(pay_per_hour), int(bonus))
print(f"Зарплата сотрудника: {salary}")
