from turtle import Turtle, Screen
import random



# 이벤트 리스너 예제
# def move_forwards제):
#     tim.forward(10)


# screen.listen()
# screen.onkey(key="space", fun=move_forwards)

# screen.exitonclick()


## 에치어 스케치
# 로직
# 1. W 키 앞으로 이동 S키 뒤로 이동 A키 시계 반대방향 회전 D키 시계방향 회전 C키 초기 상태로 돌리기


# def move_forward():
#     tim.fd(10) 
# def move_back():
#     tim.bk(10)
# def move_clock():
#     tim.lt(10)
# def move_counter_clock():
#     tim.rt(10)
# def clear():
#     tim.reset()

# screen.listen()
# screen.onkey(key="a", fun=move_counter_clock)
# screen.onkey(key="d", fun=move_clock)
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_back)
# screen.onkey(key="c", fun=clear)


# 거북이 경주 만들기
# def create_turtle(name, x, y):
#     color = colors.pop(0)
#     name = Turtle(shape="turtle")
#     name.penup()
#     name.goto(x, y)
#     name.color(color)

# create_turtle("timmy", -230, 90)
# create_turtle("jimmy", -230, 60)
# create_turtle("uimmy", -230, 30)
# create_turtle("oimmy", -230, -30)
# create_turtle("qimmy", -230, -60)
# create_turtle("eimmy", -230, -90)


## 거북이 경주 만들기


screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title="Who is the winner", prompt="Color of the turtle: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
is_race_on = False
all_turtles = []

for turtle_index in range(0, 6):
    # 동일한 객체를 여러번 생성 할 수 있다.
    # new_turtle 이라는 네임은 그냥 object 네임일 뿐 어차피 print 시 메모리 번지를 출력해줌
    # 크게 신경 안써도 어차피 다른 오브젝트로 인식함.
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)

if user_input :
    is_race_on = True

while is_race_on :
    for turtle in all_turtles:
        rand_move = random.randint(0, 20)
        turtle.forward(rand_move)
        if turtle.xcor() > 230:
            win_color = turtle.pencolor()
            if win_color == user_input :
                print(f"Winner turtle is {win_color} you bet {user_input}. \nYou Win!")
            else:
                print(f"Winner turtle is {win_color} you bet {user_input}. \nYou Lose!")
            is_race_on = False
    

screen.exitonclick()