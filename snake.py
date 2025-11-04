from turtle import Turtle

### --- SNAKE BODY --- ###
START_POS = [(0, 0), (-20, 0), (-40, 0)] # Starting position of each snake segments, CONSTANTS

### --- SNAKE BODY --- ###
MOVE_DIST = 20

### --- SNAKE TURN DIRECTIONS --- ###
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):  # ATTRIBUTES FOR OUR SNAKE CLASS
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    ### ---METHOD FOR SNAKE CLASS --- ###
    def create_snake(self):
        for pos in START_POS:  # Ea snake segments will move into a new position of the previous snake segments
            self.add_seg(pos)

    ### --- METHOD FOR ADDING SEGMENTS OF SNAKE --- ###
    def add_seg(self, pos):
        new_seg = Turtle(shape="square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(pos)
        self.segments.append(new_seg)


    ### --- METHOD FOR INCREASING SNAKE LENGTH --- ###
    def extend(self):
        self.add_seg(self.segments[-1].position())


    ### --- METHOD FOR MOVEMENT OF SNAKE --- ###
    def move(self):
        for seg_n in range(len(self.segments) - 1, 0, -1): #
            new_x = self.segments[seg_n - 1].xcor() # 2nd last segment x coord
            new_y = self.segments[seg_n - 1].ycor() # 2nd last segment y coord
            self.segments[seg_n].goto(new_x, new_y) # Last segment going to the 2nd last segment coordinates
        self.head.forward(MOVE_DIST)


    ### --- RESET SNAKE --- ###
    def reset(self):
        for seg in self.segments:
                seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]


    ### --- METHOD FOR TURNING SNAKE IN CARDINAL DIRECTIONS --- ###
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)