# наследование


# родительский класс
class Transport:
    def transport_method(self):
        print("method from Transport")


# дочерний класс
class Auto(Transport):
    def auto_method(self):
        print("method from Auto")


class Bus(Transport):
    def bus_method(self):
        print("method from Bus")


a = Auto()
a.auto_method()
a.transport_method()

b = Bus()
b.transport_method()
b.bus_method()


# class Shape:
#     def __init__(self, color, param1, param2):
#         self.color = color
#         self.param1 = param1
#         self.param2 = param2
#
#     def square(self):
#         return self.param1 * self.param2
#
#
# class Rectangle(Shape):
#     def __init__(self, color, param1, param2):
#         super().__init__(color, param1, param2)
#
#     def rectangle_p(self):
#         return 2 * (self.param1 + self.param2)
#
#
# class Square(Shape):
#     def __init__(self, color, param1):
#         Shape.__init__(self, color, param1, param1)
#
#     def square_p(self):
#         return 4 * self.param1
#
#
# r = Rectangle("white", 10, 2)
# print(r.color)
# print(r.square())
# print(r.rectangle_p())
#
# s = Square("black", 5)
# print(s.color)
# print(s.square())
# print(s.square_p())


# несколько родителей у одного класса
class Player:
    def player_method(self):
        print("method from Player")


class Navigator:
    def navigator_method(self):
        print("method from Navigator")


class Phone(Player, Navigator):
    def phone_method(self):
        print("method from Phone")


p = Phone()
p.navigator_method()
p.player_method()
p.phone_method()


class Shape:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def get_params(self):
        return f"Параметры Shape: {self.param1}, {self.param2}"


class Material:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def get_params(self):
        return f"Параметры Material: {self.param1}, {self.param2}"

    def material_method(self):
        return f"Параметры Material: {self.param1}, {self.param2}"


class Rectangle(Shape, Material):
    def __init__(self, param1, param2, param3, param4):
        # super().__init__(param1, param2)
        Shape.__init__(self, param1, param2)
        # Rectangle теперь обладает self.param1, self.param2, self.get_params
        # Material.__init__(self, param3, param4)
        # переопределение переменных
        print(Shape.get_params(self))
        print(Material.get_params(self))
        # pass


r = Rectangle(10, 2, 3, 4)
# print(r.get_params())
# print(r.material_method())
