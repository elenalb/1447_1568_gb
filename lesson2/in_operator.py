# тернарный оператор

# condition_if_true if condition else condition_if_false
# (condition_if_false, condition_if_true)[condition]

test_list = [1, 2, 3]
test_list2 = [1, 2]
all_elements_in = False
for element in test_list2:
    # с применением тернарного оператора:
    all_elements_in = True if element in test_list else False
    # all_elements_in = (False, True)[element in test_list]

    # без применения тернарного оператора:
    # if element not in test_list:
    #     all_elements_in = False
    # else:
    #     all_elements_in = True
print(all_elements_in)

print(True or "some")
print(False or "some")

func_return = None
message = func_return or "Функция ничего не вернула"
print(message)
