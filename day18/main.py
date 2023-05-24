## 터틀 모듈을 이용한 그래픽 작업


from turtle import Turtle, Screen
import random

tim = Turtle()
tim.color("red")
screen = Screen()


# 과제 1
# 1. turtle 이용해서 정사각형 그리기
# 2. 한 변의 길이가 100, 화면 어느 지점에 그리던 상관 없음

# for i in range(4):
#   tim.forward(100)
#   tim.left(90)

# 과제 2
# 1. 점선 그리기
# 2. 선그리기(10) 안그리고걸어가기(10) 를 15회 반복하시오
# xscore = 0
# for i in range(15):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)

# 과제 3
# 1. 정삼각형, 정사각형, 정오각형, 정육각형, 정칠각형, 정팔각형, 정구각형, 정십각형 그리기
# 2. 거리는 100 컬러는 도형을 다 그리고 바뀐다.
# color = ["red",
#          "royal blue",
#          "black",
#          "dark green",
#          "pink",
#          "indigo",
#          "cyan"]

# for i in range(3, 10):
#     # 외각을 구하는 방법은 360에서 변의 개수를 나눈다
#     angle = 360 / i
#     for j in range(i):
#         tim.forward(100)
#         tim.right(angle)
#     tim.color(random.choice(color))

# 과제 4
# 1. 무작위로 가는 길을 그린다.
# 2. 동쪽 서쪽 남쪽 북쪽을 무작위로 움직임 
# 3. 굴기 변경 및 선 그리는 속도 빠르게

# color = ["red",
#          "royal blue",
#          "black",
#          "dark green",
#          "pink",
#          "indigo",
#         ]
# angle = [
#     0,
#     90,
#     180,
#     270
# ]

# tim.pensize(15)
# tim.speed('fast')

# while True:
#     tim.forward(30)
#     tim.seth(random.choice(angle))
#     tim.color(random.choice(color))

# 과제 5
# 1. 스피로 그래프 그리기
# 2. 반지름이 100 인 원을 그리기

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple

tim.speed('fastest')
screen = Screen()
for angle in range(0, 360, 2):
    screen.colormode(255)
    tim.color(random_color())
    tim.circle(100)
    tim.home()
    tim.left(angle)
screen.exitonclick()

# 과제 6
# 허스트 페인팅 프로젝트
# 이미지에서 RGB 값 추출하기


