import math
class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def circle_area(self):
        return math.pi * self.radius**2

class Point:
    def __init__(self, x,y):
        self.x = x
        self.y = y
        