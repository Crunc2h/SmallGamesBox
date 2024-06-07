from turtle import Turtle
START_POS = 900
SPEED = 40
SCALE_Y = 6
SCALE_X = 2
SHAPE = "square"
COLOR = "white"


class Paddle(Turtle):
    def __init__(self, player_modifier):
        super().__init__()
        self.shape(SHAPE)
        self.color(COLOR)
        self.shapesize(stretch_wid= SCALE_Y, stretch_len= SCALE_X)
        self.penup()
        self.goto(START_POS * (-1 if player_modifier == "1" else 1), 0)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + SPEED)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - SPEED)
