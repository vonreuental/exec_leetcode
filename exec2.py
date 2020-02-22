"""
    分形树绘制图
"""
# coding=utf-8
import turtle


def pout(len):
    count = 0

    while count < 5:
        turtle.forward(len)
        turtle.right(144)
        count += 1
    len += 50
    if len < 300:
        pout(len)


def pTree(size,kuan):
    if size > 10:
        turtle.fd(size)

        turtle.right(25)
        turtle.pensize(kuan)
        pTree(size - 25,kuan - 1)


        turtle.left(50)
        turtle.pensize(kuan)
        pTree(size - 25,kuan - 1)

        turtle.right(25)
        turtle.bk(size)


turtle.left(90)
turtle.penup()
turtle.bk(300)
turtle.pendown()
turtle.speed(10)
turtle.pensize(10)

pTree(180,10)

turtle.exitonclick()
