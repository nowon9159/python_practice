# 처음 input 값으로 값 숫자를 고른다.
# 행위를 고르고 (사칙연산)
# 숫자와 연산하기위한 또 다른 숫자를 선택함
# 수식과 답을 표현 하고
# y를 타이핑 하면 계산된 답으로 다시 계산할지 n을 타이핑하면 새로운 계산을 할지 선택



first_number = input("What's the first number?: ")
value_operation = input("+\n-\n*\n/\nPick an operation: ")
next_number = input("What's the next number?: ")

check_continue = input("Type 'y' to continue calculating with {} or type 'n' to start a new claculation: ")

value_continue = False

while not value_continue :
    