from turtle import Turtle
FONT = ("Arial", 18, "normal")
ALIGNMENT = "center"
COLOR = "red"


class Display(Turtle):

    def __init__(self):
        super().__init__()
        self.color(COLOR)
        self.penup()
        self.hideturtle()

    def write_at_pos(self, x, y, content):
        self.goto(x, y)
        self.clear()
        self.write(content, False, ALIGNMENT, FONT)

    def display_level(self, level):
        self.write_at_pos(-240, 340, f"Level: {level}")

    def display_game_over(self):
        self.write_at_pos(0, 0, "GAME OVER!")
