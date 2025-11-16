import turtle
import time
import random

delay = .1
Width = 620
Height = 620

# set up the screen
wn = turtle.Screen()
wn.title("Sname Game Tutorial")
wn.bgcolor("green")
wn.setup(width=Width, height=Height)

# Snake Food
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "up"

# Snake Food

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(random.randint(-300, 300), random.randint(-300, 300))


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

    if head.distance(food) < 20:
        # Move food to new spot
        food.goto(random.randint(-300, 300), random.randint(-300, 300))

    move()

    if head.xcor == Width * -1:
        False
