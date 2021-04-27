import math

x1 = float(input('Please enter x1: '))
y1 = float(input('Please enter y1: '))
x2 = float(input('Please enter x2: '))
y2 = float(input('Please enter y2: '))

distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
inside_the_shoresh = (x1 - x2) ** 2 + (y1 - y2) ** 2
final_distance = inside_the_shoresh ** 0.5
print('The distance is :', distance)
