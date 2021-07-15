# выявление ошибок при работе с файлами

try:
    with open("text") as f:
        for line in f:
            print(line)
except FileNotFoundError:
    print("Файла не существует!")
else:
    print("Все нормально!")
finally:
    print("Блок finally")

# FileNotFoundError, IOError, FileExistsError etc
