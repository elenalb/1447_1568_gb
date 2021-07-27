# @staticmethod


class Auto:
    @staticmethod
    def get_class_info():
        print("Class Auto")


Auto.get_class_info()


class MyClass:
    @staticmethod
    def sum_1(param1, param2):
        return param1 + param2

    def sum_2(self, param1, param2):
        return param1 + param2

    def sum_3(self, param1, param2):
        return MyClass.sum_1(param1, param2)


print(MyClass.sum_1(1, 2))
mc = MyClass()
print(mc.sum_1(1, 2))
print(mc.sum_2(1, 2))
print(mc.sum_3(1, 2))


# @classmethod
class MyClass1:
    @classmethod
    def my_method(cls, param):
        print(cls, param)


MyClass1.my_method(30)
mc1 = MyClass1()
mc1.my_method(90)
