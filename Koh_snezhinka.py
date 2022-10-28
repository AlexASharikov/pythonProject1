import turtle

length = 390
n = int(input())

turtlePen = turtle.Turtle()
window = turtle.Screen()


def snezhinka(length, n):
    if n == 0:
        turtlePen.forward(length)
    else:
        snezhinka(length / 3, n - 1)
        turtlePen.left(60)
        snezhinka(length / 3, n - 1)
        turtlePen.right(120)
        snezhinka(length / 3, n - 1)
        turtlePen.left(60)
        snezhinka(length / 3, n - 1)

for i in range (0,3):
    snezhinka(length, n)
    turtlePen.right(120)

window.mainloop()