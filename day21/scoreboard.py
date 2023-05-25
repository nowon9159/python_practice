from turtle import Turtle

ALIGN = "center"
FONT = ('Courier', 24, "normal")

class Scoreboard(Turtle) :
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0,260)
        self.write_score()
        self.hideturtle()

    def write_score(self):
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGN, font=FONT)

    def get_score(self):
        self.clear()
        self.score += 1
        self.write_score()

    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"Game Over.", move=False, align=ALIGN, font=FONT)