from turtle import Turtle

USER_POSITION = [(-350, -40), (-350, -20), (-350, 0), (-350, 20), (-350, 40)]
ENEMY_POSITION = [(350, -40), (350, -20), (350, 0), (350, 20), (350, 40)]

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.init_enemy_paddle(ENEMY_POSITION)
        self.init_user_paddle(USER_POSITION)

    def init_enemy_paddle(self, position):
        for position in ENEMY_POSITION:
            self.add_segment(position)

    def init_user_paddle(self, position):
        for position in USER_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        self.paddle = Turtle(shape="square")
        self.paddle.goto(position)
        self.paddle.penup()
        self.paddle.color("white")

    # def move(self):


    # def up(self):

    # def down(self):
