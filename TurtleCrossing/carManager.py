from car import Car
import random
LANE_WIDTH = 50
LANES_MAX_Y = 300
LANES_MIN_Y = -200
CAR_BREAK_DISTANCE = 75


class CarManager:

    def __init__(self):
        self.level = 1
        self.cars = []
        self.lane_positions = []
        self.previous_lane_positions = []
        self.set_lane_positions(LANES_MIN_Y, LANES_MAX_Y)
        self.min_car_speed = 8
        self.car_speed_variance = 10
        self.max_cars_in_level = 7

    def set_lane_positions(self, min_y, max_y):
        num_of_lanes = (max_y - min_y) // LANE_WIDTH
        for n in range(num_of_lanes + 1):
            lane_position = min_y + n * LANE_WIDTH
            self.lane_positions.append(lane_position)

    def spawn_car(self):

        if len(self.previous_lane_positions) == len(self.lane_positions):
            self.previous_lane_positions.clear()

        can_spawn_in_this_lane = False
        lane_position = 0
        while not can_spawn_in_this_lane:
            lane_position = random.choice(self.lane_positions)
            if len(self.previous_lane_positions) == 0:
                can_spawn_in_this_lane = True
            else:
                for n in range(len(self.previous_lane_positions)):
                    if self.previous_lane_positions[n] == lane_position:
                        break
                    elif n == len(self.previous_lane_positions) - 1:
                        can_spawn_in_this_lane = True
        self.previous_lane_positions.append(lane_position)

        speed = self.min_car_speed + random.random() * self.car_speed_variance
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        car = Car(speed, color, lane_position)
        self.cars.append(car)

    def keep_spawning_cars(self):
        if len(self.cars) < self.max_cars_in_level:
            self.spawn_car()

    def move_cars(self):
        for car in self.cars:
            car.move()

    def manage_car_speeds(self):
        for car in self.cars:
            cars_in_the_same_lane = [car]
            for other_car in self.cars:
                if car.ycor() == other_car.ycor():
                    cars_in_the_same_lane.append(other_car)
            for other_car in cars_in_the_same_lane:
                if car.distance(other_car) < CAR_BREAK_DISTANCE:
                    car.speed = other_car.speed

    def manage_car_viability(self):
        for car in self.cars:
            if not car.check_viability():
                self.cars.remove(car)

    def manage_cars(self):
        self.move_cars()
        self.manage_car_viability()
        self.manage_car_speeds()
        self.keep_spawning_cars()

    def increase_difficulty(self):
        self.level += 1
        self.min_car_speed += 1
        self.car_speed_variance += 5
        self.max_cars_in_level += 2

