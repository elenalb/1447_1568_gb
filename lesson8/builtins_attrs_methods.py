# встроенные атрибуты и методы объектов класса


class User:
    """
    Class contains user info
    """
    def __init__(self, name, login, password):
        self.name = name
        self.login = login
        self.password = password

    def get_user_data(self):
        return f"Name: {self.name}, login: {self.login}, password: {self.password}"


u = User("Ivan", "ivan_ivan", "qwerty")
print(u.get_user_data())
print(f"__name__: {User.__name__}\n__module__: {User.__module__}\n"
      f"__dict__: {User.__dict__}\n"
      f"__dict__: {u.__dict__}\n"
      f"__doc__: {User.__doc__}\n"
      f"__init__: {User.__init__}\n__class__: {User.__class__}")
