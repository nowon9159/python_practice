## 정의
# 뜨거운 커피를 뽑는 기계를 디지털로 만들자
# 커피의 종류 별로 가격, 재료가 다르다
# 커피 머신에 들어가는 원재료는 수시로 채워줘야한다.
# 커피 머신을 동작하기 위해 동전이 필요한데 Penny : 1 cent ($0.01) Dime : 10 cents ($0.10) Nickel : 5 cents ($0.05) Quagrter : 25 cents ($0.25) 이다.

## 로직
# 필요한 것
# 1. 보고서를 출력할 수 있어야 한다.
# -> 어떤 재료가 얼마나 남았는 지 , 물은 얼마나 있고, 우유는 얼마나 남았는 지를 알 수 있어야 한다.
# -> input에 report 를 입력하면 Water, Milk, Coffee, Money 를 출력하고 인풋 다시 받기 # espresso/latte/cappuccino
# 2. 사용자가 커피를 주문할 때 재료가 충분한지 확인하는 기능도 필요하다.
# -> 사용자가 라떼를 주문했다고 가정했을 때 동전을 넣으면 거스름돈이 나오고 라떼도 나온다. 보고서를 확인하면 물이 100ml 밖에 없는 것 확인 가능
# -> 이런 경우에서 물이 필요한데 채워 넣지 않고 주문을 하면 죄송합니다 문구 출력
# 3. 동전을 처리할 수 있어야 한다.
# -> 동전을 종류별로 넣어서 커피의 가격보다 낮은 가격의 동전을 넣게 되면 커피는 나오지 않고 동전은 반환 된다. # Sorry that's not enough money. Money refunded.
# -> 커피의 가격보다 높은 가격의 동전을 넣게 되면 커피 가격을 기준으로 거스름돈을 주게 된다.

import data

resources = {
    "water": 300, # ml
    "milk": 200, # ml
    "coffee": 100, # g
}

cost = {
    "cent": 1,
    "dime": 10,
    "nickel": 5,
    "quarter": 25
}

today_take = 0

def check_cost(quaters_input, dimes_input, nickels_input, cents_input) :
    quaters_input
    dimes_input
    nickels_input
    cents_input
    return 




while True :
    
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    print("Please insert coins.")
    quaters_input = input("how many quarters?: ")
    dimes_input = input("how many dimes?: ")
    nickels_input = input("how many nickels?: ")
    cents_input = input("how many cents?: ")

    check_cost(quaters_input, dimes_input, nickels_input, cents_input)

    print(f"Here is ${} in change.")
    print(f"Here is your espresso ☕. Enjoy!")


