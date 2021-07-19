# классы, объекты, атрибуты


# CamelCase - для имен классов
class Auto:
    # атрибуты класса
    auto_name = "Lexus"
    auto_model = "123"
    auto_year = 2005

    # методы класса
    def auto_start(self):
        print("Заводим автомобиль")

    def auto_stop(self):
        print("Останавливаем автомобиль")


# auto = Auto()  # экземпляр / объект класса Auto
# print(auto)
# print(auto.auto_name)
# auto.auto_start()
# auto.auto_stop()
#
# auto1 = Auto()
# print(auto1.auto_year)


class Auto1:
    # атрибуты класса
    count = 0

    # методы класса
    def auto_start(self, auto_name, auto_model, auto_year):
        # атрибуты экземпляра
        self.auto_name = auto_name
        self.auto_model = auto_model
        self.auto_year = auto_year
        print("Заводим автомобиль")
        Auto1.count += 1

    def auto_stop(self):
        print("Останавливаем автомобиль")


a = Auto1()
a.auto_start("BMW", "123", 1999)
print(a.auto_name)
print(a.count)

a1 = Auto1()
a1.auto_start("Mazda", "123", 2008)
print(a1.auto_name)
print(a1.count)

print(a.count)  # атрибуты класса одинаковы для всех объектов класса!
