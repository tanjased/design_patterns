from math import *


# FACTORY METHOD
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Coordinates: {self.x}, {self.y}'

    @staticmethod
    def cartesian(x, y):
        return Point(x, y)

    @staticmethod
    def polar(rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))


if __name__ == '__main__':
    p1 = Point.cartesian(2, 3)
    p2 = Point.polar(2, 3)
    print(p1, '\n', p2)


# FACTORY
# the idea of implementation of SRP. Once you get too many factory method in the class,
# it might make sense to move them out of the class. or at least group them
# So basically we move all @staticmethods from previous example to a new class
# The details for the other developer that there's a (point) factory can be specified only in the documentation.
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Coordinates: {self.x}, {self.y}'

    # We put this class into the Point class. When it's like this, there's no need of @staticmethod, but self must be put into ()
    class PointFactory:
        def cartesian(self, x, y):
            p = Point()
            p.x = x
            p.y = y
            return p

        def polar(self, rho, theta):
            return Point(rho * cos(theta), rho * sin(theta))

    factory = PointFactory()  # an instance of a factory can also be created


# and here we change Point.polar(2, 3) to Point.PointFactory.polar(2, 3)
if __name__ == '__main__':
    p1 = Point(2, 3)
    p2 = Point.PointFactory.polar(2, 3)
    print(p1, '\n', p2)

## factory is a class full of factory methods (not necessarily static ones) which allow you to create an object!



