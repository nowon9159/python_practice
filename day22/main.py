## 퐁 게임 만들기
## 로직

# 각각의 클래스로 분리
# 1. 적 컴퓨터 패들
# 1.1 패들은 일정 속도로 위아래로 움직인다.
# 2. 내가 조종할 수 있는 패들
# 2.1 키보드 위 아래 버튼으로 움직일 수 있음
# 3. 스코어 보드
# 3.1 상대방 구역에 공이 위치하면 내가 스코어를 얻고
# 내 구역에 공이 위치하면 상대방이 스코어를 얻는다
# 4. 움직이는 공
# 4.1 움직인다 어떻게? 대각선 일정 각도로 그런데 X축 끝 벽에 부딪히면 튕겨져 나감 어떻게? 일정 각도로
# 4.2 패들에 공이 부딪히면 공이 튕겨 나간다

from turtle import Screen
from paddle import Paddle
from ball import Ball
import random
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("#000000")
screen.title("My Pong Game!")
screen.tracer(0)

USER_POSITION = (-350, 0)
ENEMY_POSITION = (350, 0)

user_paddle = Paddle(USER_POSITION)
enemy_paddle = Paddle(ENEMY_POSITION)

ball = Ball()

screen.listen()

screen.onkey(key="Up", fun=enemy_paddle.go_up)
screen.onkey(key="Down", fun=enemy_paddle.go_down)
screen.onkey(key="w", fun=user_paddle.go_up)
screen.onkey(key="s", fun=user_paddle.go_down)

while True:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce_y()

    if ball.distance(enemy_paddle) < 50 and ball.xcor() > 320 or ball.distance(user_paddle) < 50 and ball.xcor() < -320 :
        ball.bounce_x()

screen.exitonclick()


