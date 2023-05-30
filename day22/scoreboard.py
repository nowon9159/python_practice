from turtle import Turtle

ALIGN = "center"
FONT = ('Courier', 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"Game Over.", move=False, align=ALIGN, font=FONT)