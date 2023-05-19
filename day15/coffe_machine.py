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
# -> 동전을 종류별로 넣어서 커피의 가격보다 낮은 가격의 동전을 넣게 되면 커피는 나오지 않고 동전은 반환 된다.
# -> 커피의 가격보다 높은 가격의 동전을 넣게 되면 커피 가격을 기준으로 거스름돈을 주게 된다.
menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# 현재 남은 리소스 선언
resources = {
    "water": 300, # ml
    "milk": 200, # ml
    "coffee": 100, # g
}

# 오늘 매출액
today_take = 0

## 커피 만드는 로직 재 정리
# 1. 어떤 커피인지 알아야 함 -> 함수 선언 시 input 값 파라미터로 받아서 함수 안에서 체크
# 2. 해당 커피를 만들 때 드는 리소스 비용을 현재 리소스 비용과 비교해야함.
# -> 어떤 커피인지 체크 후에 리소스 얼마 남았는 지 비교
# 2.1 비교해서 리소스 비용이 더 많으면 진행 적으면 return false
def can_make(user_input):
    for item in user_input:
        if user_input[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def make_coffee(items, user_input):
    for item in items:
        resources[item] -= items[item]
    print(f"Here is your {user_input} ☕. Enjoy!")

def check_changes(ingre_coffee, user_input, quaters_input, dimes_input, nickels_input, cents_input):
    cost = menu[user_input]['cost']
    all_cost = (quaters_input * 0.01) + (dimes_input * 0.1) + (nickels_input * 0.05) + (cents_input * 0.25)
    result_cost = all_cost - cost
    if all_cost > cost :
        print(f"Here is ${result_cost} in change.")
        make_coffee(ingre_coffee, user_input)
        global today_take
        today_take += cost
    else :
        print("Sorry that's not enough money. Money refunded.")
        return False

while True :
    # 오늘 번 돈
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['water']}g")
        print(f"Money: ${today_take}")
    else:
        coffee = menu[user_input]
        if can_make(coffee['ingredients']) :
            print("Please insert coins.")
            quaters_input = int(input("how many quarters?: "))
            dimes_input = int(input("how many dimes?: "))
            nickels_input = int(input("how many nickels?: "))
            cents_input = int(input("how many cents?: "))
            check_changes(coffee['ingredients'], user_input, quaters_input, dimes_input, nickels_input, cents_input)