# 처음 input 값으로 값 숫자를 고른다.
# 행위를 고르고 (사칙연산)
# 숫자와 연산하기위한 또 다른 숫자를 선택함
# 수식과 답을 표현 하고
# y를 타이핑 하면 계산된 답으로 다시 계산할지 n을 타이핑하면 새로운 계산을 할지 선택




# 첫째로 사칙 연산에 대한 함수를 설정하세요

def add(n1, n2):
    return n1 + n2

def minus(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def devide(n1, n2):
    return n1 / n2

# 둘 째로 사칙 연산을 딕셔너리에 집어 넣으세요.
# 키에는 연산의 기호를 밸류에는 연산의 이름을

operation = {
    "+" : add,
    "-" : minus,
    "*" : multiply,
    "/" : devide,
}

# 셋 째로 연산에 필요한 인풋 값을 받겠습니다.

num1 = input("What's the first number?: ")
num2 = input("")