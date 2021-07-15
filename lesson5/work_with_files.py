# работа с файлами

f = open("test_file.txt", "r")
# f_obj = open(r"C:\Users\elena.babenko\PycharmProjects\1447_1568_gb\lesson5\test_file.txt")

# read()
content = f.read()
print(content)
print(type(content))
f.close()

# readline()
# line_1 = f.readline()
# line_2 = f.readline()
# print(line_1, line_2)
# f.close()

# readlines()
# content = f.readlines()
# print(content)
# f.close()

# чтение файла по частям
# for line in f:
#     print(line)
#
# f.close()

# ограничение количества считываемых символов
# while True:
#     content = f.read(10)
#     print(content)
#
#     if not content:
#         break

# чтение бинарных файлов
# my_f = open("text", "rb")

# запись данных в файл
# write()
new_f = open("new_text_file", "w")
new_f.write("new string in file")
new_f.close()

# writelines()
new_f = open("new_text_file", "w")
new_f.writelines(["new string in file\n", "second line"])
new_f.close()
