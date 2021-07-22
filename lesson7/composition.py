# композиция
# len_1 * height, len_2 * height
# S = 2 * height * (len_1 + len_2) - windows - doors


class WindowDoor:
    def __init__(self, wd_len, wd_height):
        self.square = wd_height * wd_len


class Room:
    def __init__(self, len_1, len_2, height):
        self.square = 2 * height * (len_1 + len_2)
        self.wd = []

    def add_wd(self, wd_len, wd_height):
        self.wd.append(WindowDoor(wd_len, wd_height))

    def common_square(self):
        main_square = self.square
        for wd in self.wd:
            main_square -= wd.square
        return main_square


r = Room(10, 5, 3)
print(r.square)
r.add_wd(2.5, 1.5)
r.add_wd(1, 1)
r.add_wd(1, 1)
print(r.common_square())
print(r.wd)


# __init__.py
