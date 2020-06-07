import turtle

def SquareSpiral(lineLen, myTurtle):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        SquareSpiral(lineLen - 5, myTurtle)
        
screen = turtle.Screen()
yertle = turtle.Turtle()
SquareSpiral(200, yertle)