import math

point_dist = 0.0

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

''' Your solution goes here '''
point_dist = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
print('Points distance:', point_dist)