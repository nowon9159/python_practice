## 목표
# 뱀 게임 만들기
# 1. 뱀의 몸통 만들기 -> 화면에 사각형 세 개를 나란히 붙이면 된다.
# 2. 뱀을 이동하는 법을 알아야함
# 3. 키보드로 뱀을 조종하는 법을 알아야함.
# 4. 먹이를 감지하고 먹이를 먹었을 시 몸통이 늘어나야함
# 5. 스코어를 알 수 있는 스코어 보드가 있어야함.
# 6. 벽과 부딪힐 시 게임 오버
# 7. 꼬리와 부딪힐 시 게임 오버

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#000000")
screen.title("My Snake Game!")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

while True :
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        print("nom nom nom")
        food.refresh()
        scoreboard.get_score()
        snake.extend()
    
    if snake.head.xcor() > 290 or snake.head.ycor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290:
        scoreboard.game_over()
        screen.exitonclick()
        break

    