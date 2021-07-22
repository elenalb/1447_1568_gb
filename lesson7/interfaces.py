# интерфейсы
from abc import ABC, abstractmethod


class MyAbstractClass(ABC):
    @abstractmethod
    def my_method_1(self):
        pass

    @abstractmethod
    def my_method_2(self):
        pass


class MyClass(MyAbstractClass):
    def my_method_1(self):
        print("my_method_1()")

    def my_method_2(self):
        print("my_method_2()")

    def my_method(self):
        pass


mc = MyClass()
mc.my_method_1()
