# turtle graphic 객체 연습하기

import another_module

print(another_module.another_variable)

from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
# 과제 1. 거북이 색깔 바꾸기
timmy.color("red")

my_screen = Screen()
print(my_screen.canvheight)

my_screen.exitonclick()