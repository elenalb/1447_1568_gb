"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми
значениями, то новый элемент с тем же значением должен разместиться после них.

Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""
rating = [7, 5, 3, 3, 2]
print(rating)
keep_going = True
while keep_going:
    user_num = int(input('Введите свое место: '))
    rating.append(user_num)
    rating.sort()
    rating.reverse()
    print(rating)
    user_answer = input("Хотите продолжить? Для остановки наберите 'нет'. ")
    if user_answer == 'нет':
        keep_going = False
print(rating)