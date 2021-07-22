# интерфейс итерации
# for in, map(), zip()

my_list = [30, 10, 'hello', True]
for element in my_list:
    print(element)


# 1. __iter__() для списка my_list
# my_list.__iter__()
# 2. в for in вызывается метод __next__()
# 3. StopIteration, когда элементы итератора закончились


class Iterator:
    """
    объект-итератор
    """
    def __init__(self, start=0):
        self.i = start

    def __next__(self):
        self.i += 1
        if self.i <= 5:
            return self.i
        else:
            raise StopIteration


class IterObj:
    """
    объект, который поддерживает интерфейс итерации
    """
    def __init__(self, start=0):
        self.start = start - 1

    def __iter__(self):
        return Iterator(self.start)


obj = IterObj(start=3)
for el in obj:
    print(el)
print(list(obj))
for el in obj:
    print(el)


class Iter:
    def __init__(self, start=0):
        self.i = start - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i <= 5:
            return self.i
        else:
            raise StopIteration


iterobj = Iter(start=2)
for i in iterobj:
    print(i)

print(list(iterobj))
