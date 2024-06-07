import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
WIDTH = 1920
HEIGHT = 1080
WALL_HEIGHT_Y = 520
AI_Y_MAX = 450
MIN_DISTANCE_TO_PADDLE = 50
MIN_X_FOR_COLLISION = 875


def create_screen():
    screen = Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("pong")
    screen.bgcolor("black")
    screen.tracer(0)
    screen.listen()
    return screen


def determine_ai_mode(ai_paddle, current_mode):
    if ai_paddle.ycor() >= AI_Y_MAX:
        return "down"
    elif ai_paddle.ycor() <= -AI_Y_MAX:
        return "up"
    else:
        return current_mode


def ai_movement(ai_paddle, current_mode):
    if current_mode == "up":
        ai_paddle.move_up()
    else:
        ai_paddle.move_down()


screen = create_screen()
paddle_1 = Paddle("1")
paddle_2 = Paddle("2")
ai_mode = "up"
screen.onkeypress(key='w', fun=paddle_1.move_up)
screen.onkeypress(key='s', fun=paddle_1.move_down)
ball = Ball()
while True:
    ai_mode = determine_ai_mode(paddle_2, ai_mode)
    ai_movement(paddle_2, ai_mode)
    ball.move()
    if ball.ycor() >= WALL_HEIGHT_Y or ball.ycor() <= -WALL_HEIGHT_Y:
        ball.bounce_y()
    if ball.xcor() > MIN_X_FOR_COLLISION or ball.xcor() < -MIN_X_FOR_COLLISION:
        if ball.distance(paddle_1) < MIN_DISTANCE_TO_PADDLE or ball.distance(paddle_2) < MIN_DISTANCE_TO_PADDLE:
            ball.bounce_x()
    screen.update()
    time.sleep(0.05)



