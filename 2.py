import turtle

def koh(l, n):
    if n == 0:
        turtle.forward(l)
        return

    x = l/3
    # for i in range(n):
    koh(x, n-1)
    turtle.left(60)
    koh(x, n-1)
    turtle.right(120)
    koh(x, n-1)
    turtle.left(60)
    koh(x, n-1)


turtle.penup()
turtle.goto(-300, 0)
turtle.pendown()
koh(400,3)
