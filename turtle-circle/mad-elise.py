import turtle

def drawPolygon(t, sideLength, numSides):
    turnAngle = 360 / numSides
    for i in range(numSides):
        t.forward(sideLength)
        t.left(turnAngle)

def drawFilledCircle(anyTurtle, radius):
    circumference = 2 * 3.1415 * radius
    sideLength = circumference / 360
    anyTurtle.fillcolor("violet")
    anyTurtle.begin_fill()
    drawPolygon(anyTurtle, sideLength, 360)
    anyTurtle.end_fill()

wn = turtle.Screen()
wheel = turtle.Turtle()

wheel.left(90)
wheel.penup()
wheel.forward(20)
wheel.left(90)
wheel.pendown()
wheel.speed(0)

drawFilledCircle(wheel,20)

wn.exitonclick()
