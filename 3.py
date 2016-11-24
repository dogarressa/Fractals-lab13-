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
def snowflake(l, n):
    x = l/3
    for i in range(3):
        koh(x, n-1)
        turtle.left(60)
        koh(x, n-1)
        turtle.right(120)
        koh(x, n-1)
        turtle.left(60)
        koh(x, n-1)
        turtle.right(120)

turtle.penup()
turtle.goto(-200, 100)
turtle.pendown()
snowflake(200, 3)
