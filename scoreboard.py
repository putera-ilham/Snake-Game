from turtle import Turtle

### --- CONSTANTS --- ###
ALIGNMENT =  "CENTER"
FONT = ("Arial", 24, "normal")


### --- Score Presentation --- ###
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.goto(0, 260)
        self.color("white")
        self.penup()
        self.update_scoreboard()
        self.hideturtle()


    ### --- Update score --- ###
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)


    ### --- Increase score after snake eats --- ###
    def increase_score(self):
        self.score += 1
        self.clear() # Clears previous scores preventing overlap scores
        self.update_scoreboard()


    ### --- UPDATE OF HIGH SCORE WHEN USER REACHES A HIGHER SCORE THAN PREVIOUS --- ###
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()



    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER!!", align=ALIGNMENT, font=FONT)

