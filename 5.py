import turtle

def levi(l, n):
    if n == 0:
        turtle.forward(l)
        return
    x=l*0.5*(2**0.5)
    turtle.left(45)
    levi(x, n-1)
    turtle.right(90)
    levi(x, n-1)
    turtle.left(45)

turtle.penup()
turtle.goto(-100, 0)
turtle.pendown()
levi(200,10)
