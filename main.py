import turtle
import time

delay = .05
Width = 650
Height = 650

# set up the screen
wn = turtle.Screen()
wn.title("Sname Game Tutorial")
wn.bgcolor("green")
wn.setup(width=Width, height=Height)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "up"


# Functions
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "right":

        x = head.xcor()
        head.setx(x + 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)


def goingUp():
    if head.direction == "down":
        return
    else:
        head.direction = "up"


def goingDown():
    if head.direction == "up":
        return
    else:
        head.direction = "down"


def goingRight():
    if head.direction == "left":
        return
    else:
        head.direction = "right"


def goingLeft():
    if head.direction == "right":
        return
    else:
        head.direction = "left"


# Key bindings
wn.listen()
wn.onkeypress(goingDown, "s")
wn.onkeypress(goingUp, "w")
wn.onkeypress(goingRight, "d")
wn.onkeypress(goingLeft, "a")

# Main game loop
while True:
    wn.update()
    time.sleep(delay)
    move()
