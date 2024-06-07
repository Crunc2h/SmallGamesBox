from snake import Snake
from food import Food
from scoreboard import Scoreboard
from turtle import Screen
from time import sleep
WIDTH = 600
HEIGHT = 600
X_LIMIT = 280
Y_LIMIT = 280
SCREEN_COLOR = "black"
TITLE = "Snaking"


def create_screen():
    screen = Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title(TITLE)
    screen.bgcolor(SCREEN_COLOR)
    screen.tracer(0)
    screen.listen()
    return screen


def take_input(l_snake, screen):
    screen.onkey(key='a', fun=l_snake.turn_left)
    screen.onkey(key='d', fun=l_snake.turn_right)
    screen.onkey(key='w', fun=l_snake.turn_up)
    screen.onkey(key='s', fun=l_snake.turn_down)


def check_collision_with_food(l_snake, l_food):
    if l_snake.head.distance(l_food) < 20:
        return True
    return False


def check_collision_with_body(l_snake):
    for segment in l_snake.body[1::]:
        if l_snake.head.distance(segment) < 10:
            return False
    return True


def check_collision_with_walls(l_snake):
    if (l_snake.head.xcor() > X_LIMIT or l_snake.head.xcor() < -X_LIMIT
            or l_snake.head.ycor() > Y_LIMIT or l_snake.head.ycor() < -Y_LIMIT):
        return False
    return True


game_screen = create_screen()
snake = Snake()
take_input(snake, game_screen)
food = Food()
scoreboard = Scoreboard()
scoreboard.refresh_score()


while True:
    snake.move()
    if check_collision_with_food(snake, food):
        snake.extend_body()
        food.refresh_food_pos()
        scoreboard.score += 1
        scoreboard.refresh_score()

    f_reset = False if not check_collision_with_body(snake) or not check_collision_with_walls(snake) else True
    if not f_reset:
        scoreboard.reset()
        snake.reset()
    game_screen.update()
    sleep(0.1)

