import turtle

def minkovsky(l, n):
    if n == 0:
        turtle.forward(l)
        return

    x = l/4

    minkovsky(x, n-1)
    turtle.left(90)
    minkovsky(x, n-1)
    turtle.right(90)
    minkovsky(x, n-1)
    turtle.right(90)
    minkovsky(x, n-1)
    minkovsky(x, n-1)
    turtle.left(90)
    minkovsky(x, n-1)
    turtle.left(90)
    minkovsky(x, n-1)
    turtle.right(90)
    minkovsky(x, n-1)




turtle.penup()
turtle.goto(-300, 0)
turtle.pendown()
minkovsky(400,1)
