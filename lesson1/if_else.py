# ветвления

a = int(input("Введите число: "))

if a % 2 == 0:
    if a > 10:
        print("a > 10")
    print("a is even!")  # блок кода 1
else:
    print("a is odd")  # блок кода 2


colour = "pink"
if colour == "blue":
    print("синий")
elif colour == "green":
    print("зеленый")
elif colour == "red":
    print("красный")
else:
    print("Неизвестный цвет")
