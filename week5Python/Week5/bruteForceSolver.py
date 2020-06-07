''' Read in first equation, ax + by = c '''
a = int(input())
b = int(input())
c = int(input())

''' Read in second equation, dx + ey = f '''
d = int(input())
e = int(input())
f = int(input())

haveSolution = False

for x in range(-10, 11):
    for y in range(-10, 11):
        x1 = float((c - b * y) / a)
        x2 = float((f - e * y) / d)
        y1 = float((c - a * x) / b)
        y2 = float((f - d * x) / e)
        if(x1 == x2 and y1 == y2):
            print(x, y)
            haveSolution = True
if(haveSolution == False):
    print("No solution")
''' Type your code here. '''