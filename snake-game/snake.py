from turtle import Turtle

BODY_LEN = int(20)
SEG_LEN = 6
DEFAULT_SIZE = 20


class Snake:
    def __init__(self):
        self.segment = []
        self.build_snake()
        self.head = self.segment[0]
        self.body_len = BODY_LEN

    def build_snake(self):
        starting_x = []
        for seg in range(0, SEG_LEN):
            new_x = -1 * seg * BODY_LEN
            starting_x.append([new_x, 0])

        for position in starting_x:
            self.add_seg(position)
            # new_segment = Turtle(shape="square")
            # new_segment.shapesize(BODY_LEN / DEFAULT_SIZE, BODY_LEN / DEFAULT_SIZE)
            # new_segment.penup()
            # new_segment.color("white")
            # new_segment.goto(position)
            # self.segment.append(new_segment)

    def move_snake(self):
        for segment_num in range(len(self.segment)-1, 0, -1):
            new_xcor = self.segment[segment_num - 1].xcor()
            new_ycor = self.segment[segment_num - 1].ycor()
            self.segment[segment_num].goto(new_xcor, new_ycor)
        self.head.forward(BODY_LEN)

    def add_seg(self, position):
        new_segment = Turtle(shape="square")
        new_segment.shapesize(BODY_LEN / DEFAULT_SIZE, BODY_LEN / DEFAULT_SIZE)
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segment.append(new_segment)

    def extend_body(self):
        self.add_seg(self.segment[-1].position())
        # new_segment = Turtle(shape="square")
        # new_segment.shapesize(BODY_LEN / DEFAULT_SIZE, BODY_LEN / DEFAULT_SIZE)
        # new_segment.penup()
        # new_segment.color("white")
        # new_segment.goto(position, 0)
        # self.segment.append(new_segment)

    def up(self):
        if self.segment[0].heading() != 270:
            self.segment[0].setheading(90)

    def down(self):
        if self.segment[0].heading() != 90:
            self.segment[0].setheading(270)

    def left(self):
        if self.segment[0].heading() != 0:
            self.segment[0].setheading(180)

    def right(self):
        if self.segment[0].heading() != 180:
            self.segment[0].setheading(0)








