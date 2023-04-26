# 비밀 경매 프로그램 제작
#
# 보통 경매는 모두가 입찰을 할 수 있고 모두의 입찰가를 볼 수 있습니다
# 그리고 경매인은 여러분들이 더 높은 입찰가를 부르도록
# 유도합니다 그리고 가장 높은 입찰가가 정해져서 경매가 끝날 때까지 다른 사람이 얼마를 입찰했는지
# 모르는 경매인 비밀 경매라는 것이 있습니다 이번엔 그 프로그램을 만들어보도록 하겠습니다

# 1. 로고 출력 / 이름 입력, 입찰가 입력
# 2. 다른 입찰인 있는지 yes or no
#     2.1 if yes 라면 스크린 초기화 하고 이름과 입찰가 입력
#     2.2 if no 라면 누가 가장 높은 입찰가를 입력 했는 지 확인하고 낙찰인과 낙찰가 출력

# 2번은 반복 로직 입찰인 있는지 체크 -> 있다면 반복문으로 이름과 입찰가 입력
# 반복문으로 입력한 이름과 입찰가를 Key Value 형식으로 딕셔너리에 저장
# Value 값만 뽑아내 가장 큰 수를 체크
# 가장 큰 수가 낙찰가가 되며 변수에 저장 후, 낙찰가의 값으로 Key 를 뽑아내 낙찰인을 변수에 저장


import os
from art import logo

def clear() : 
    os.system("cls") # 화면 초기화

print(logo)
print("Welcome to the secret auction program.")

bids = {}
continue_value = False

def pick_highest(bidding_record) :
    highest_bid = 0
    # for문을 이용해서 bidding_record 라는 파라미터를 받아서 해당하는 딕셔너리의 키를 돌려 bid_amount 에 집어 넣는다
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder] # 왜냐하면 딕셔너리의 각 키를 이용해서 bid_amount 를 바꿔주기 때문에 -> 여러 값을 담는 게 아니라 계속 바꿔준다
        # 만약 bid_amount (여기서 bid_amount는 입찰자의 가격) 가 highest_bid 보다 크다면 highest_bid 를 bid_amount 로 교체 
        # 예를 들어 123 을 입찰자가 집어 넣었다면 당연히 0보다 123 이 크기 때문에 123이 highest_bid 가 된다.
        # 그 후로 누군가 123 보다 큰 수를 넣게 되면 highest_bid 가 변경됨
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            # 누군가 현재 최고가 보다 큰 수를 넣게 되면 그 누군가를 winner로 지정함
            winner = bidder
    print(f"{winner} is {highest_bid}")

while not continue_value :
    name = input("What is your name? \n")
    price = int(input("What's your bid? \n$"))
    bids[name] = price # 오브젝트는 objname[key] = value 로 값을 집어넣을 수 있음
    have_others = input("Are there any other bidders? Type 'yes' or 'no'. \n")
    # input 값 받아서 key value 형식으로 dictionary 에 저장
    if have_others == "yes" :
        continue_value = False
        clear()
    elif have_others == "no" :
        continue_value = True
        pick_highest(bids)
  
