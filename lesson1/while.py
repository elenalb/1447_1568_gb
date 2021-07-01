# цикл while

number = int(input("Введите число: "))

while number < 10:
    print(number)
    number += 1  # number = number + 1
print("Цикл завершен")

# break, continue

i = 0
while True:
    i += 1
    if i > 10:
        break
    if i % 2 == 0:
        continue
    print(i)
