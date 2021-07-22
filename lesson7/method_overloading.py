# переопределение методов


class ParentClass:
    def __init__(self, param, var):
        print(f"Конструктор класса {__class__.__name__}")
        self.param = param
        self.var = var
        self._protected = 'hello'
        self.__private = 'private'

    def my_method(self):
        print("Метод my_method() родительского класса")


class ChildClass(ParentClass):
    def __init__(self, param, var):
        print(f"Конструктор класса {__class__.__name__}")
        super().__init__(param, var)
        # ParentClass.__init__(self)

    def my_method(self):
        ParentClass.my_method(self)
        # super().my_method()
        print("Метод my_method() дочернего класса")


c = ChildClass(10, 'var')
c.my_method()
print(c.var)
print(c._protected)
