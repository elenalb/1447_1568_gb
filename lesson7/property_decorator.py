# декоратор @property


class MyClass:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    @property
    def my_method(self):
        return f"Атрибуты экземпляра класса {__class__.__name__}: " \
               f"self.param1 = {self.param1}, self.param2 = {self.param2}"

    @property
    def name(self):
        return f"name.{self.param1}"


mc = MyClass(10, 2)
print(mc.param2)
print(mc.my_method)


# 2000-2021
class Auto:
    def __init__(self, year):
        self.year = year

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if year < 2000:
            self.__year = 2000
        elif year > 2021:
            self.__year = 2021
        else:
            self.__year = year

    def get_auto_year(self):
        return f"Автомобиль выпущен в {self.year} году"


a = Auto(2100)
print(a.get_auto_year())
