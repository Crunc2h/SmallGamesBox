from turtle import Screen
from carManager import CarManager
from player import Player, SPAWN_Y
from display import Display
from time import sleep
HEIGHT = 840
WIDTH = 620
BACKGROUND_COLOR = "gray"
TITLE = "Turtle Crossing"
LEVEL_UP_Y = 320


def create_screen():
    screen = Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.tracer(0)
    screen.listen()
    screen.bgcolor(BACKGROUND_COLOR)
    screen.colormode(255)
    screen.title(TITLE)
    return screen


def check_collisions_with_player(cars_in_level, l_player):
    for car in cars_in_level:
        if (abs(car.xcor() - l_player.xcor()) < 35 and
                (l_player.ycor() <= car.ycor() + 20 and l_player.ycor() >= car.ycor() - 20)):
            print("hit")
            return False
    return True


game_screen = create_screen()
display = Display()
car_manager = CarManager()
display.display_level(car_manager.level)
player = Player()
game_screen.onkeypress(key='Up', fun=player.move)
f_continue = True
while f_continue:
    car_manager.manage_cars()
    if player.ycor() >= LEVEL_UP_Y:
        car_manager.increase_difficulty()
        player.goto(player.xcor(), SPAWN_Y)
        display.display_level(car_manager.level)
    game_screen.update()
    f_continue = check_collisions_with_player(car_manager.cars, player)
    sleep(0.05)
display.display_game_over()
game_screen.exitonclick()
