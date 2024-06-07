from turtle import Turtle
SHAPE = "square"
SPAWN_X = 400
SCALE_X = 1
SCALE_Y = 2.5


class Car(Turtle):

    def __init__(self, speed, color, spawn_y):
        super().__init__()
        self.speed = speed * -1
        self.shape(SHAPE)
        self.shapesize(SCALE_X, SCALE_Y)
        self.color(color)
        self.penup()
        self.goto(SPAWN_X, spawn_y)
        self.is_viable = True

    def move(self):
        self.goto(self.xcor() + self.speed, self.ycor())

    def check_viability(self):
        if self.xcor() < -420:
            return False
        return True

