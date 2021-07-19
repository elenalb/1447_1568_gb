# конструктор, методы
# области видимости


class Auto:
    # атрибут класса - глобальные переменные
    count = 0
    num_wheels = 4

    def __init__(self, auto_name, auto_year):
        Auto.count += 1
        self.auto_name = auto_name
        self.auto_year = auto_year

    def get_class_info(self):
        print(f"Марка автомобиля: {self.auto_name}, год выпуска: {self.auto_year}")

    def auto_start(self):
        info = "info"  # локальная переменная
        return info


a1 = Auto("Mazda", 2005)
a1.get_class_info()
print(a1.auto_start())
# print(a1.info) -- нет доступа к локальной переменной через объект класса!
a2 = Auto("BMW", 1995)
a2.get_class_info()
a3 = Auto("Toyota", 1999)
a3.get_class_info()

# ctrl + /
