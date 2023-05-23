## 터틀 모듈을 이용한 그래픽 작업


## 로직
#

from turtle import Turtle, Screen

tim = Turtle()
tim.shape("circle")
tim.color("red")


# 과제 1
# 1. turtle 이용해서 정사각형 그리기
# 2. 한 변의 길이가 100, 화면 어느 지점에 그리던 상관 없음

# for i in range(4):
#   tim.forward(100)
#   tim.left(90)


# 과제 2
# 1. 점선 그리기
# 2. 선그리기(10) 안그리고걸어가기(10) 를 15회 반복하시오

for i in range(15):
    tim.forward(10)
    tim.setpos(10,0)


screen = Screen()
screen.exitonclick()