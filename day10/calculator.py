# 처음 input 값으로 값 숫자를 고른다.
# 행위를 고르고 (사칙연산)
# 숫자와 연산하기위한 또 다른 숫자를 선택함
# 수식과 답을 표현 하고
# y를 타이핑 하면 계산된 답으로 다시 계산할지 n을 타이핑하면 새로운 계산을 할지 선택
# y를 타이핑 한 두번째 연산 부터는 first_number의 인풋 값을 받지 않고 연산 된 값을 first_number로 대체

value_continue = True
value_after_2ndoperation = "False"
operation_number = 0


first_number = int(input("What's the first number?: "))
value_operation = input("+\n-\n*\n/\nPick an operation: ")
next_number = int(input("What's the next number?: "))

check_continue = input(f"Type 'y' to continue calculating with {first_number} or type 'n' to start a new claculation: ")

value_continue = False

def add(first_number, next_number):
    return first_number + next_number

def minus(first_number, next_number):
    return first_number - next_number

def multiply(first_number, next_number):
    return first_number * next_number

def divide(first_number, next_number):
    return first_number / next_number

while not value_continue :
    if value_operation == "+":
        return first_number + next_number
    elif value_operation == "-":
        minus(first_number, next_number)
    elif value_operation == "*":
        multiply(first_number, next_number)
    elif value_operation == "/":
        return first_number / next_number
    else :
        print("You Put a Wrong Input.")

while value_continue :
    if value_after_2ndoperation == "True" :
        first_number = operation_number
    elif value_after_2ndoperation == "False" :
        first_number = int(input("What's the first number?: ")) # 첫째 값 받는다

    value_operation = input("+\n-\n*\n/\nPick an operation: ") # 어떤 연산을 할 지 고르기
    next_number = int(input("What's the next number?: ")) # 둘째 값 받는다
    
    
