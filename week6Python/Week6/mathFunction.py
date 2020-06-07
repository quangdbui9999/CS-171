import math

x = 4.7
y = 5.3
z = -4.8
a = -3.2
print(math.ceil(x)) # 5
print(math.ceil(y)) # 6
print(math.ceil(z)) # (-4)
print(math.ceil(a)) # (-3)
print(math.floor(x)) # 4
print(math.floor(y)) # 5
print(math.floor(z)) # (-5)
print(math.floor(a)) # (-4)

import math

def calculateArea(radius):
    area = math.pi * radius ** 2
    print("A circle of Radius %d has Area %.2f" %(radius, area))

def calculateDiameter(radius):
    diameter = radius * 2
    print("The diameter of a circle is: %.2f" %diameter)
    
def main():
    radius2 = int(input("Enter the radius: "))
    calculateDiameter(radius2)
    calculateArea(radius2)
    #calculateArea(6)
    #calculateDiameter(8)

main()
