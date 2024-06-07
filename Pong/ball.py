from turtle import Turtle
SHAPE = "circle"
COLOR = "white"
SIZE = 1
SPEED =-10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.shapesize(SIZE)
        self.color(COLOR)
        self.ball_speed_x = SPEED
        self.ball_speed_y = SPEED
        self.penup()

    def move(self):
        self.goto(self.xcor() + self.ball_speed_x, self.ycor() + self.ball_speed_y)

    def bounce_y(self):
        self.ball_speed_y *= -1

    def bounce_x(self):
        self.ball_speed_x *= -1










