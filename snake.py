import turtle
import time


def jobbra():
    fej.right(90)


def balra():
    fej.left(90)


palya = turtle.Screen()
palya.setup(width=800, height=600)
palya.bgcolor("green")
palya.title("Snake")
palya.tracer(0)
palya.listen()
palya.onkey(jobbra, "Right")
palya.onkey(balra, "Left")

fej = turtle.Turtle()
fej.shape("triangle")
fej.penup()
fej.color("yellow")

szöveg = turtle.Turtle()
szöveg.color("white")
szöveg.hideturtle()
szöveg.penup()
szöveg.goto(-100, 225)

while True:
    fej.forward(20)
    if fej.ycor() > 300 or fej.ycor() < -300 or fej.xcor() > 400 or fej.xcor() < -400:
        fej.clear()
        szöveg.write("A kukac megdöglött", font=("Arial", 20, "bold"))

    palya.update()
    time.sleep(0.3)

