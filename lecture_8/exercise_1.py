import math


# Last LECTURE!!!
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other_point):
        # other_point is going to be of type point
        return math.sqrt((self.x - other_point.x) ** 2 +
                         (self.y - other_point.y) ** 2)

    def get_textual_representation_of_myself(self):
        return '({},{})'.format(self.x, self.y)


point1 = Point(1, 1)
point2 = Point(3, 5)
print('The distance between point {} and point {} is {}'
      .format(point1.get_textual_representation_of_myself(),
              point2.get_textual_representation_of_myself(),
              point1.distance(point2)))

point3 = Point(5, 11)
point4 = Point(11, 31)
pnt3_distance = point3.distance(point4)
pass
