import turtle

def BounquetFlower(line, myTurtle):
    if line > 5:
        myTurtle.forward(line)
        myTurtle.right(20)
        BounquetFlower(line - 15, myTurtle)
        myTurtle.left(40)
        BounquetFlower(line - 15, myTurtle)
        myTurtle.right(20)
        myTurtle.backward(line)
        
screen = turtle.Screen()
yertle = turtle.Turtle()
yertle.setpos(0, -100)
yertle.left(90)
BounquetFlower(100, yertle)