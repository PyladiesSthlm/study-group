import turtle 
def drawSquare(t, sz):
    """Make turtle t draw a square of sz."""
    for i in range(15):
        t.forward(sz)
        t.left(90)
        t.forward(sz)
        t.right(90)

def drawTriangle(t, sz):
    """Make turtle t draw a square of sz."""
    for i in range(3):
        t.forward(sz)
        t.left(120)

def drawOctagon(t, sz):
   for i in range(8):
        t.forward(sz)
        t.left(45)
        
def drawCircle(t, sz):
   for i in range(28):
        t.forward(sz)
        t.left(15)
        
bob = turtle.Turtle()
#drawTriangle(bob, 50)    
        
#drawSquare(bob, 5) 

#drawOctagon(bob, 50) 

drawCircle(bob, 5) 
