from turtle import Turtle
FONT = ("Arial", 18, "normal")
ALIGNMENT = "center"
COLOR = "white"
HIGHSCORE_FILE = "./highscores.txt"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.highscore = self.retreive_highscore_from_file()
        self.score = 0
        self.penup()
        self.color(COLOR)
        self.hideturtle()
        self.goto(0, 260)

    def refresh_score(self):
        self.clear()
        self.write(f"Score : {self.score}  Highscore : {self.highscore}", False, ALIGNMENT, FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.refresh_score()
        self.write_highscore_to_file()

    def display_game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", False, ALIGNMENT, FONT)

    def retreive_highscore_from_file(self):
        file = open(HIGHSCORE_FILE)
        highscore = file.read()
        file.close()
        return int(highscore)

    def write_highscore_to_file(self):
        file = open(HIGHSCORE_FILE, 'w')
        highscore_as_str = str(self.highscore)
        file.write(highscore_as_str)
        file.close()


