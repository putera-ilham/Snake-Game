from turtle import Turtle
import random

# Calling the Turtle super class into the Food class
class Food(Turtle):

    # Calling the Turtle init method into the Food init method
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh() # New food refresh

    # Random spawn location of the food
    def refresh(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)








