# 이미지를 이용한 색상 리스트 추출
# 리스트를 하나 추출했기 때문에 주석처리
# import colorgram

# colors = colorgram.extract("spot_painting.png", 30)

# extract_color = []

# for i in colors:
#     choice_r = i.rgb.r
#     choice_g = i.rgb.g
#     choice_b = i.rgb.b
#     tuple_color = (choice_r, choice_g, choice_b)
#     extract_color.append(tuple_color)
# print(extract_color)


from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.colormode(255)
screen.screensize(1080,2000)
tim.penup()
tim.ht()
tim.speed('fastest')
# 과제 2
# 가로 10줄 세로 10줄의 점을 찍어야한다.
# 각 점은 크기가 약 20 점들 간의 간격은 약 50
color_list = [(247, 249, 248), (248, 246, 245), (235, 216, 91), (232, 240, 244), (41, 108, 151), (245, 220, 232), (117, 222, 237), (243, 132, 48), (217, 124, 190), (112, 197, 119), (244, 79, 43), (229, 46, 86), (16, 173, 200), (154, 29, 33), (136, 157, 210), (169, 42, 97), (248, 164, 213), (136, 68, 51), (14, 179, 96), (79, 113, 204), (74, 41, 35), (0, 117, 73), (49, 44, 59), (19, 65, 154), (113, 224, 211), (126, 37, 35), (234, 171, 161), (46, 125, 92), (21, 85, 103), (173, 182, 220)]
def get_color():
    return color_list[random.randint(0, len(color_list)-1)]

for i in range(0,100):
    tim.dot(20, get_color())
    tim.forward(50)
    print(tim.position())
    for j in range(0,10):
        if tim.position() == (float(500), float(j*50)):
            tim.home()
            tim.sety(float((j+1)*50))

screen.exitonclick()
