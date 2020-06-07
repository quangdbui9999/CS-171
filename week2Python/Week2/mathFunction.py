''' Type your code here. '''
import math

class LoveMath:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def process(self):
        self.x = math.sqrt(self.x)
        self.y = math.fabs(self.y - self.z)
        self.z = self.calculate_factorial(math.ceil(self.z))
    
    def calculate_factorial(self, number):
        if number <= 1:
            return 1
        else:
            return number * self.calculate_factorial(number - 1)
        
    def output(self):
        return "{:.2f} {:.2f} {:.2f}".format(self.x, self.y, self.z)

whoLoveMath = LoveMath(x = float(input()), y = float(input()), z = float(input()))
whoLoveMath.process()
print(whoLoveMath.output())