# 1. TypeError: can only concatenate str (not "int") to str
# my_var = int(input("Введите число: ")) + 5
# print(my_var)

# 2. SyntaxError: invalid syntax
# msg = True
# if msg == True:
#     print("True")

# 3. SyntaxError: invalid syntax
# msg = True
# if msg == True:
#     print("True")

# 4. NameError: name 'my_var' is not defined
# my_var = 1
# print(my_var)

# 5. IndentationError: expected an indented block
# my_var = True
# if my_var == True:
#     print("True")

# 6. TabError: inconsistent use of tabs and spaces in indentation
# my_var = True
# if my_var == True:
#     print("пробелы")
#     print("tab")

# 7. UnboundLocalError: local variable 'my_var' referenced before assignment
def my_func(my_var):
    my_var += 1
    print(my_var)


my_var = 10
my_func(my_var)
