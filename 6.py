import turtle

def dragon(l, n):
    if n == 0:
        turtle.forward(l)
        return
    x=l*0.5*(2**0.5)



    turtle.right(45)
    dragon(x, n-1)
    turtle.left(90)
    dragon(x, n-1)




turtle.penup()
turtle.goto(-100, 0)
turtle.pendown()
dragon(200, 2)
