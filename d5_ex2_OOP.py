# în Python totul este un obiect.
# înseamnă că totul este derivat dintr-o clasă.

class MyClass:
    pass

class MyClass:
    def mymethod(self):
        print(self)

    def __repr__(self):
        return "MyClass()"


from math import sqrt

class Point:
    # semnătura unei clase este dată de metoda
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def get_distance_from_origin(self):
        return sqrt(self.x ** 2 + self.y ** 2)

# decorator care are sens doar în context de clasă:
# @property

class Point:
    # semnătura unei clase este dată de metoda
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    # @property implementează pattern de
    # getter / setter
    @property
    def distance_from_origin(self):
        print("mă execut!")
        return sqrt(self.x ** 2 + self.y ** 2)

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return (
            self.x < other.x
            or (self.x == other.x and self.y < other.y)
        )

    def __sub__(self, other):
        # TODO:
        # return Vector(distance_between, angle)
        pass

# inheritance:
class Point3D(Point):
    def __init__(self, x, y, z):
        "DRY - don't repeat yourself"
        super().__init__(x, y)

        self.z = z

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y}, {self.z})"

    def translate(self, dx, dy, dz):
        super().translate(dx, dy)
        self.z += dz


