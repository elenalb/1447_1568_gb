# перегрузка операторов


# __init__()
# __del__()
# __str__()
# __add__() -- +
# __lt__() -- <
class MyClass:
    def __init__(self, param, digit1, digit2):
        self.param = param
        self.digit1 = digit1
        self.digit2 = digit2

    def __del__(self):
        print(f"Удаляем объект {self.param}")

    def __str__(self):
        return f"Объект с параметром {self.param}, {self.digit1}, {self.digit2}"

    def __add__(self, other):
        return MyClass(self.param + other.param, self.digit1 + other.digit1, self.digit2 + other.digit2)


mc = MyClass('param', 10, 2)
print(mc.param)
print(mc)
mc1 = MyClass('hello', 2, 22)
print(mc + mc1)


class Salary:
    val = 50000

    def __lt__(self, other):
        print("Оклад меньше премии?")
        return self.val < other.val


class Prize:
    val = 5000

    def __lt__(self, other):
        print("Премия меньше оклада?")
        return self.val < other.val


s = Salary()
p = Prize()

check = s < p
print(check)
print(p < s)

