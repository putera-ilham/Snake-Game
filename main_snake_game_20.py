import time
from turtle import Screen

from scoreboard import Scoreboard
from snake import Snake
from food import Food



### --- SCREEN SETUP --- ###
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Ze Snake Game")
screen.tracer(0)


### --- CALLING THE SNAKE, FOOD CLASS TO INITIALISE THE SNAKE --- ###
snakey = Snake()
food = Food()
scoreboard = Scoreboard()


### --- KEYPRESS TO CONTROL THE SNAKE --- ###
screen.listen()
screen.onkey(snakey.up, "Up")
screen.onkey(snakey.down, "Down")
screen.onkey(snakey.left, "Left")
screen.onkey(snakey.right, "Right")


### --- SNAKE MOVEMENT --- ###
game_on = True
while game_on:
    screen.update() # REMOVE BUFFER AND MAKE ACTION LOOKS CONTINUOUS
    time.sleep(0.125) # FRAME RATE CONTROL - DELAYS THE LOOP SO THAT SNAKE IS VISIBLE


    ### --- CALLING THE SNAKE CLASS TO MOVE THE SNAKE --- ###
    snakey.move()


    ### --- COLLISION BETWEEN FOOD & SNAKE --- ###
    ### --- INCREASING SNAKE LENGTH --- ###
    if snakey.head.distance(food) < 15:
        food.refresh()
        snakey.extend()
        scoreboard.increase_score()


    ### --- COLLISION BETWEEN WALL & SNAKE --- ###
    if snakey.head.xcor() > 280 or snakey.head.xcor() < -280 or snakey.head.ycor() > 280 or snakey.head.ycor() < -280:
        scoreboard.reset()
        snakey.reset()


    ### --- COLLISION BETWEEN WALL & SNAKE --- ###
    for segments in snakey.segments[1:]:
        if snakey.head.distance(segments) < 10:
            scoreboard.reset()
            snakey.reset()


### --- SCREEN EXIT --- ###
screen.exitonclick()