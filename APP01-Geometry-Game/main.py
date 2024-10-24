import turtle

# Create a canvas instance
myTurtle = turtle.Turtle()

# go to a certain coordinate
myTurtle.penup()
myTurtle.goto(50, 75)

myTurtle.pendown()
myTurtle.forward(100) # move 100 pixels
myTurtle.left(90) # turn left 90 degrees
myTurtle.forward(200)
myTurtle.left(90)
myTurtle.forward(100)
myTurtle.left(90)
myTurtle.forward(200)


turtle.done()