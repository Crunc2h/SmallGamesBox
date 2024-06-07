from turtle import Screen
from turtle import Turtle
from pandas import read_csv
from time import sleep
from math import atan2, degrees
with open("50_states.csv") as state_data_file:
    state_data = read_csv(state_data_file)
FONT = ("Arial", 10, "normal")
ALIGNMENT = "center"


def create_screen():
    screen = Screen()
    screen.setup(725, 491)
    screen.tracer(0)
    screen.bgpic("blank_states_img.gif")
    screen.title("Guess The State")
    return screen


def take_user_input(screen):
    return screen.textinput(f"Found {len(states_already_found)}/50 states", "Name a state:").title()


def validate_user_input(l_user_input, l_state_data, states_found):
    return True if l_user_input in l_state_data["state"].values and l_user_input not in states_found else False


def find_state_properties(l_user_input, l_state_data):
    state_name = [state for state in l_state_data["state"].values if l_user_input == state][0]
    state_coordinates = (l_state_data[l_state_data["state"] == state_name].x.item(),  l_state_data[l_state_data["state"] == state_name].y.item())
    return state_name, state_coordinates


class StateWriter(Turtle):

    def __init__(self, state_name, position):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.speed = 1
        self.position = position
        self.state_name = state_name
        self.turn_to_state(self.position)

    def move(self):
        self.clear()
        self.fd(self.speed)
        self.write(self.state_name, False, ALIGNMENT, FONT)

    def turn_to_state(self, position):
        angle = degrees(atan2(position[1], position[0])) % 360
        self.left(angle)


game_screen = create_screen()
states_already_found = []
f_continue = True
while f_continue:
    user_input = take_user_input(game_screen)

    while validate_user_input(user_input, state_data, states_already_found) is False:
        user_input = take_user_input(game_screen)
        game_screen.update()
        sleep(0.01)

    state_name_and_coord = find_state_properties(user_input, state_data)
    states_already_found.append(state_name_and_coord[0])
    state_writer = StateWriter(state_name_and_coord[0], state_name_and_coord[1])

    while state_writer.distance(state_name_and_coord[1][0], state_name_and_coord[1][1]) > 1:
        state_writer.move()
        game_screen.update()
        sleep(0.01)

    f_continue = False if len(states_already_found) == len(state_data["state"]) else True

state_writer = StateWriter("YOU WON!", (0,0))



