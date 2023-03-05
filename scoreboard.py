from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.goto(x=-280, y=250)
        self.hideturtle()
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Level: {self.score},", align="left", font=FONT)
    def add_score(self):
        self.score += 1
        self.write_score()

    def game_over(self):
        self.goto(-50,0)
        self.write("GAME OVER", align="left", font=FONT)