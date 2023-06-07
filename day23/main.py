## 로직
# 크로시 로드라는 인디게임과 비슷함
# 엄청나게 많은 차들이 다차선 고속도로를 바쁘게 지나고 있고
# 거북이는 그걸 피해서 반대쪽 까지 가는 게 목표
# 반대쪽 까지 가면 위치는 초기화 레벨은 올라가고 차들의 속도는 빨라진다.
# 거북이는 앞으로만 갈 수 있음

from car import car
from user_turtle import user_turtle
from turtle import Turtle
from turtle import Screen
from scoreboard import Scoreboard
import random
import time


screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("#000000")
screen.title("My Pong Game!")
screen.tracer(0)

my_turtle = user_turtle()

while True :
    time.sleep(0.1)
