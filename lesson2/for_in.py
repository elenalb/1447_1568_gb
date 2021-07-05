# цикл for in

# for [переменная-итератор] in [последовательность]:
#     [действия, выполняемые для каждой переменной]

for element in "string":
    print(element)

my_tuple = (1, 2, 3)
my_list = []
for element in my_tuple:
    my_list.append(element)
print(my_list)

my_dict = {1: 'one', 2: 'two'}
for key, value in my_dict.items():
    print(key, value)

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

digit = 9

for line in matrix:
    if digit in line:
        print(f"Число {digit} находится в {matrix.index(line) + 1} строке!")
