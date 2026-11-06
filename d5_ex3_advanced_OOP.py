# getter / setter cu @property

class BankAccount:
    def __init__(self):
        self.__balance = 0

    def __repr__(self):
        return f"BankAccount(balance={self.balance})"

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Account balance can't be negative")
        self.__balance = value

# @classmethod
# face ca primul argument al metodei să fie obiectul-clasă
class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"MyClass({self.x}, {self.y})"

    @classmethod
    def create_from_tuple(cls, tup):
        # this is a "factory method"
        return cls(tup[0], tup[1])

# ce classmethods am mai întâlnit?
# datetime.date.today()
# datetime.datetime.now()
# dict.fromkeys(iterable)

# @staticmethod
# transformă metoda într-o funcție obișnuită

def compute_stuff(a, b):
    return a + b

class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"MyClass({self.x}, {self.y})"

    def regular_method(self):
        print(self.compute_stuff(self.x, self.y))

    @staticmethod
    def compute_stuff(a, b):
        return a + b


# item access
class MyCollection:
    def __getitem__(self, key):
        return "wow, o valoare"

    def __setitem__(self, key, value):
        pass


# making it into an iterable:
class MyIterableIterator:
    def __next__(self):
        pass

class MyIterable:
    def __iter__(self):
        # we must return an object
        # that supports next()
        return MyIterableIterator(self.my_collection)

# but we usually do this:
import random

class MyRandomGenerator:
    def __init__(self, min, max, count):
        self.min = min
        self.max = max
        self.count = count

        self._counter = 0

    def __iter__(self):
        return self

    def __len__(self):
        return self.count

    def __next__(self):
        self._counter += 1
        if self._counter > self.count:
            raise StopIteration()

        return random.randint(self.min, self.max)


# să facem un context manager:
class CtxManager:
    def __init__(self, x):
        self.x = x

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        # cleanup
        print("i am cleaning up, even if there was an exception")


# multiple inheritance issues:
class GeometryBase:
    def translate(self, coordinates):
        print("» I am", "GeometryBase.translate")

class BiDimensionalObject:
    def as_coordinates(self):
        print("» I am", "BiDimensionalObject.as_coordinates")


class MyPoint(GeometryBase, BiDimensionalObject):
    pass

# what about overriding parent methods?
# but what happens during diamond inheritance?
class Ancestor:
    def method(self):
        print("» I am", "Ancestor.method")

class ParentOne(Ancestor):
    def method(self):
        Ancestor.method(self)
        print("» I am", "ParentOne.method")

class ParentTwo(Ancestor):
    def method(self):
        Ancestor.method(self)
        print("» I am", "ParentTwo.method")

class Child(ParentOne, ParentTwo):
    def method(self):
        ParentOne.method(self)
        ParentTwo.method(self)
        print("» I am", "Child.method")

# problem statement:
# during multiple inheritance, ancestor methods
# get run twice.

# solution: introducing...
# super() -- resolves the current object
#            in the context of the parent class(es)

class Ancestor:
    def method(self):
        print("» I am", "Ancestor.method")

class ParentOne(Ancestor):
    def method(self):
        super().method()
        self.attr = 25
        print("» I am", "ParentOne.method")

class ParentTwo(Ancestor):
    def method(self):
        super().method()
        self.attr = 0
        print("» I am", "ParentTwo.method")

class Child(ParentOne, ParentTwo):
    def method(self):
        super().method()
        print("» I am", "Child.method")
