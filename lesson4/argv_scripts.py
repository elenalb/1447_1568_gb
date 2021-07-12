# запуск скрипта с параметрами

from sys import argv

script_name, first_param, second_param, third_param = argv

print(f"Имя скрипта: {script_name}")
print(f"Первый параметр: {first_param}")
print(f"Второй параметр: {second_param}")
print(f"Третий параметр: {third_param}")
