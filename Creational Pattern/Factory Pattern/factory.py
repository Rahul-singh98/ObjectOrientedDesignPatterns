import math


class Shape:

    def __init__(self):
        pass

    def resize(self):
        pass

    def draw(self):
        pass


class Rectangle(Shape):

    def __init__(self, l, b):
        self._l = l
        self._b = b

    def draw(self):
        l = self._l + (self._l/2)
        for row in range(self._b):
            if (row == 0 or row == self._b-1):
                print("* " * self._l)
            else:
                print("*" + (" " * (self._l + 2)) + "*")


class Circle(Shape):

    def __init__(self, r):
        self._r = r

    def draw(self):
        for i in range((2 * self._r)+1):
            for j in range((2 * self._r)+1):
                dist = math.sqrt((i - self._r) * (i - self._r) +
                                 (j - self._r) * (j - self._r))
                if (dist > self._r - 0.5 and dist < self._r + 0.5):
                    print("*", end="")
                else:
                    print(" ", end="")
            print()


class Triangle(Shape):

    def __init__(self, l):
        self._l = l

    def draw(self):
        m = (2 * self._l) - 2
        for i in range(0, self._l):
            for j in range(0, self._l):
                print(end=" ")
            self._l = self._l - 1
            for j in range(0, i + 1):
                print("*", end=' ')
            print(" ")

    def rough(self):
        print("Rough")


class ShapeFactory:

    def getShape(self, shape_name: str) -> Shape:
        shape = None
        shape_name = shape_name.lower()

        if shape_name == "rectangle":
            shape = Rectangle(5, 4)
        elif shape_name == "circle":
            shape = Circle(5)
        elif shape_name == "square":
            shape = Rectangle(5, 5)
        elif shape_name == "triangle":
            shape = Triangle(5)

        return shape


if __name__ == "__main__":
    factory = ShapeFactory()
    print("Welcome to the terminal")
    while True:
        user_input = input("Write shape name or q for quit : ")
        if user_input == 'q':
            break

        shape = factory.getShape(user_input)
        if shape:
            shape.draw()
        else:
            "Invalid Shape"
            break

    print("GoodBye")
