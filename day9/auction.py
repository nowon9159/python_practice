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

import os
from art import logo

os.system("cls") # 화면 초기화

print(logo)
print("Welcome to the secret auction program.")
user_name = ""
user_bid = ""
have_others = "yes"

dict_price = {}
list_price = []
list_price_ascending = []

def auction(have_others) :
    while have_others == "yes" :
        
        user_name = input("What is your name? \n")
        user_bid = input("What's your bid? \n")
        have_others = input("Are there any other bidders? Type 'yes' or 'no'. \n")

        dict_price[user_name] = user_bid
        
        # os.system("cls") # 화면 초기화
        print(dict_price)

        for i in dict_price :
            list_price[i] = dict_price[i]
        
        list_price_ascending = list_price.sort(reverse=True)
        winner = list_price_ascending.index(list_price[0])
        winner_price = list_price[0]


        if  have_others == "no" :
            print(f"The winner is ${winner} with a bid of ${winner_price}")    
            break

auction(have_others)