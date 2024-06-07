from turtle import Turtle
from random import randint
COLOR = "blue"
SHAPE = "circle"
SIZE = 0.5
COORD_MODIFIER = 13 / 30
SPAWN_X_MAX = 260
SPAWN_Y_MAX = 260


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape(SHAPE)
        self.shapesize(SIZE)
        self.color(COLOR)
        self.refresh_food_pos()

    def refresh_food_pos(self):
        random_x = randint(-SPAWN_X_MAX, SPAWN_X_MAX)
        random_y = randint(-SPAWN_Y_MAX, SPAWN_Y_MAX)
        self.goto(random_x, random_y)
