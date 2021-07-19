# полиморфизм


# перегрузка методов -- overloading
class Auto:
    def auto_start(self, param1, param2=None):
        if param2:
            return param1 + param2
        return param1


a = Auto()
print(a.auto_start(1))
print(a.auto_start(1, 2))


# переопределение методов -- overriding
class Transport:
    def show_info(self):
        print("class Transport")


class Bus(Transport):
    def show_info(self):
        print("class Bus")


class Plane(Transport):
    def show_info(self):
        print("class Plane")


t = Transport()
t.show_info()

b = Bus()
b.show_info()

p = Plane()
p.show_info()
