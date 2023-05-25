from turtle import Turtle

STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    def create_snake(self):
        # 뱀 몸통 init
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        add_segment = Turtle(shape="square")
        add_segment.color("white")
        add_segment.penup()
        add_segment.goto(position)
        self.segments.append(add_segment)

    def extend(self):
        """add a new segment to the snake"""
        self.add_segment(self.segments[-1].position())

    def move(self):
       # 뱀 이동 시 몸통 전체 이동
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
    
    # 키보드 onkey 시 이벤트 함수
    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)