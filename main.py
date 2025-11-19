import turtle
import time
import random

delay = .01
Width = 600
Height = 600
score = 0

# Boarders
maxX = Width / 2
minX = (Width / 2) * -1
maxY = Height / 2
minY = (Height / 2 * -1)

# set up the screen
wn = turtle.Screen()
wn.title("Sname Game Tutorial")
wn.bgcolor("green")
wn.setup(width=Width, height=Height)
turtle.Screen()

# Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "right"
locationX = head.xcor
print(locationX)


# Snake Food

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(random.randint(-290, 290), random.randint(-290, 290))


# Functions


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 5)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 5)

    if head.direction == "right":

        x = head.xcor()
        head.setx(x + 5)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 5)

    # while True:
    if (head.xcor() < minX
        or head.xcor() > maxX
        or head.ycor() < minY
            or head.ycor() > maxY):
        print("(", head.xcor(), ",",  head.ycor(), ")")

        # Set "X" to be true if the head.xcor() is within the parameters
        # Set "Y" to be true if the head.xcor() is within the parameters
        # If both "X" and "Y" are true, -> move().


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
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        score = score + 1
        print(score)

    # while True:

    move()
