class Rectangle:
    def __init__(self, width, height):
        self._height = height
        self._width = width

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f'Width: {self.width}, height: {self.height}'

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value


class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    # We create a decorator based on the parent class setters.
    # We need to be sure, that width and height will be the same in this class
    # That's why we define setter decorators for both width and height.
    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value


def use_it(rc):
    w = rc.width
    rc.height = 10  # unpleasant side effect. It also changes the width, that's why the result in the video is 100.
    expected = int(w * 10)
    print(f'Expected an area of {expected}, got {rc.area}')

# It works correctly. The area can't be 6 as the final height param was set in use_it() func, the last height was taken by default.
rc = Rectangle(2, 3)
use_it(rc)

# In this case when we use use_it() the method in class automatically changes the h and w to be equal
sq = Square(5)
use_it(sq)
