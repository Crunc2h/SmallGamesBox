from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
RIGHT = 0
LEFT = 180
UP = 90
DOWN = 270
SPEED = 25
SHAPE = "square"
COLOR = "green"


class Snake:
    def __init__(self):
        self.body = self.create_body()
        self.head = self.body[0]

    def create_body(self):
        body = []
        for position in STARTING_POSITIONS:
            segment = self.create_body_segment()
            body.append(segment)
            segment.goto(position)
        return body

    def create_body_segment(self):
        segment = Turtle()
        segment.shape(SHAPE)
        segment.color(COLOR)
        segment.penup()
        return segment

    def extend_body(self):
        new_segment = self.create_body_segment()
        new_segment.goto(self.body[-1].xcor(), self.body[-1].ycor())
        self.body.append(new_segment)

    def move(self):
        for segment_index in range(len(self.body)):
            self.body[::-1][segment_index].goto(self.body[::-1][segment_index + 1].xcor(),
                                                self.body[::-1][segment_index + 1].ycor()) \
                if segment_index != len(self.body) - 1 \
                else self.body[::-1][segment_index].forward(SPEED)

    def reset(self):
        for segment in self.body:
            segment.goto(1000, 1000)
        self.body.clear()
        self.body = self.create_body()
        self.head = self.body[0]

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
