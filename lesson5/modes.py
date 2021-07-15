# режимы доступа к файлу

# r - read, default in open()
# w - write, удаляет все содержимое файла, если файла нет - будет создан
# x - write, запись в файл, если его нет. Если файл есть - ошибка
# a - append, данные добавляются в конец файла
# b - binary files
# t - text files
# + - read & write

# f_1 = open("text_for_x.txt", "x")
# f_2 = open("text_for_x.txt", "x")
# f_1.close()

f_obj = open("text_for_x.txt", "a")
f_obj.write("hello")
f_obj.close()

with open("text_for_x.txt", "w+") as f:
    f.write("New line")
    content = f.read()
    print(content)

# параметры файлового объекта
# f.closed
# f.mode
# f.name
print(f_obj.name)
print(f_obj.closed)
print(f_obj.mode)

# позиция указателя в файле
with open("text_for_x.txt", "w+") as f:
    f.write("New line")
    print(f"Указатель находится на {f.tell()}")
    f.seek(0)
    print(f"Указатель находится на {f.tell()}")
    content = f.read()
    print(content)
