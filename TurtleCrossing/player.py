from turtle import Turtle
SHAPE = "turtle"
COLOR = "green"
SPAWN_Y = -300
UP = 90
SIZE = 1
SPEED = 10


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.shapesize(SIZE)
        self.color(COLOR)
        self.penup()
        self.speed = SPEED
        self.setheading(UP)
        self.goto(self.xcor(), SPAWN_Y)

    def move(self):
        self.goto(self.xcor(), self.ycor() + self.speed)
