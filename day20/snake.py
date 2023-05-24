from turtle import Turtle

STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        
    def create_snake(self):
        # 뱀 몸통 시작 만들기
        for position in STARTING_POSITION:
            self.new_segment = Turtle(shape="square")
            self.new_segment.color("white")
            self.new_segment.penup()
            self.new_segment.goto(position)
            self.segments.append(self.new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
            self.segments[0].forward(MOVE_DISTANCE)

    def 
        



# def move_up():
#     t.seth(90)
# def move_down():
#     t.seth(270)
# def move_left():
#     t.seth(180)
# def move_right():
#     t.seth(0)


# screen.listen()
# screen.onkey(key="Up", fun=move_up)
# screen.onkey(key="Down", fun=move_down)
# screen.onkey(key="Left", fun=move_left)
# screen.onkey(key="Right", fun=move_right)