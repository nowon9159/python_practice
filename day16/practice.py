# turtle graphic 객체 연습하기

# import another_module

# print(another_module.another_variable)

# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)

# timmy.shape("turtle")
# # 과제 1. 거북이 색깔 바꾸기
# timmy.color("red")
# # 과제 2. 거북이 100 걸음 앞으로 가게 하기
# timmy.forward(100)


# my_screen = Screen()
# print(my_screen.canvheight)

# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable() 
table.field_names = ["Pokemon Name", "Type"]
table.add_row(["Pikachu","Electric"])
table.add_row(["Squirtle","Water"])
table.add_row(["Charmander","Fire"])
table.align = "l"
print(table)

