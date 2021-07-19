# модификаторы доступа
# инкапсуляция

# public - публичный - auto
# protected - защищенный - _auto
# private - приватный - __auto


class Auto:
    def __init__(self):
        print("класс Auto")
        self.auto_name = "Mazda"
        self._auto_year = 1995
        self.__auto_model = "123"

    def _protected_method(self):
        print("This method is protected!")

    def __private_method(self):
        print("This method is private!")


a = Auto()
print(a.auto_name)
a.auto_name = "BMW"
print(a.auto_name)
print(a._auto_year)
a._protected_method()
# print(a.__auto_model) -- доступна только в пределах класса
a._Auto__private_method()  # доступ к приватным переменным

# инкапсуляция - механизм сокрытия данных
