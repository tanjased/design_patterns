import copy

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f' ({self.x}, {self.y})'

class Line:
    def __init__(self, start=Point(), end=Point()):
        self.start = start
        self.end = end

    def __str__(self):
        return f'Start: {self.start},\n' \
               f'End: {self.end}'

    def deep_copy(self):
        res = copy.deepcopy(Line(self.start, self.end))
        return res


p1 = Point(2,3)
p2 = Point(4,8)
l1 = Line(p1,p2)
l2 = l1.deep_copy()
l2.start = (0,1)
# print(p1)
# print(p2)
print(l1)
print(l2)