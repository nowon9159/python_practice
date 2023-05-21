## OOP를 이용한 커피 머신 만들기

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

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()

while True :
    user_input = input(f"What would you like? ({my_menu.get_items()}): ")
    if user_input == 'report':
        my_coffee_maker.report()
        my_money_machine.report()
    else:
        drink = my_menu.find_drink(user_input)
        if my_coffee_maker.is_resource_sufficient(drink=drink):
            if my_money_machine.make_payment(drink.cost) :
                my_coffee_maker.make_coffee(drink)