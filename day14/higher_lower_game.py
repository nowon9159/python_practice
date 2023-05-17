##로직
# highlowergame.com을 기반
# 어느쪽이 더 많은 인스타 팔로워 수를 가질 지 체크
# 1. 첫 시작 시 data 에서 랜덤으로 A,B 값 뽑아내기
# 2. A, B 값을 뽑아내어 이름, 팔로워 수, 설명, 나라 데이터 뽑아내기
# 3. 반복 로직 수행
#   3.1 로고 출력
#   3.2 A 데이터 출력
#   3.3 vs 로고 출력
#   3.4 B 데이터 출력
#   3.5 인풋 값 받기
#   3.6 if 인풋 값이 A 라면 A > B 인지 확인하기
#       3.6.1 A > B 가 맞다면 A 값은 놔두고 새로운 B 값 할당, 스코어를 얻었다는 문구 출력
#       3.6.2 틀리다면 모든 스코어 초기화하고, 게임 종료
#   3.7 elif 인풋 값이 B 라면 B > A 인지 확인하기
#       3.7.1 B > A 가 맞다면 B 값을 A 값으로 대체 후 스코어를 얻었다는 문구 출력
#       3.7.2 틀리다면 모든 스코어 초기화하고, 게임 종료

from game_data import data
from art import logo, vs
import os # os.system('clear')
import random 

score = 0
init_game = True

ran_data_A = random.choice(data) 
ran_data_B = random.choice(data) 

# ran_data_A != ran_data_B 처리
if ran_data_A == ran_data_B :
    ran_data_B = random.choice(data) 


""" 리팩토링 // 변수 담는 처리를 함수화 하기 """
data_A_name = ran_data_A['name'] 
data_A_follower = ran_data_A['follower_count'] 
data_A_desc = ran_data_A['description']
data_A_country = ran_data_A['country']

data_B_name = ran_data_B['name'] 
data_B_follower = ran_data_B['follower_count'] 
data_B_desc = ran_data_B['description']
data_B_country = ran_data_B['country']


while True :
    os.system('cls')
    print(logo)
    
    # 정답일 시 스코어 출력
    if score != 0 and init_game == False :
        print(f"You're right! Current score: {score}.")
    """ 함수를 이용한 print 출력 """
    print(f'Compare A: {data_A_name}, a {data_A_desc}, from {data_A_country}.')
    print(vs)
    print(f'Against B: {data_B_name}, a {data_B_desc}, from {data_B_country}.')
    
    user_input = input("Who has more followers? Type 'A' or 'B' : ")

    if user_input == 'A' and data_A_follower > data_B_follower :
        init_game = False

        ran_data_B = random.choice(data)

        data_B_name = ran_data_B['name'] 
        data_B_follower = ran_data_B['follower_count'] 
        data_B_desc = ran_data_B['description']
        data_B_country = ran_data_B['country']

        score += 1
    elif user_input == 'B' and data_A_follower < data_B_follower :
        init_game = False

        # 기존 B 값 A 값으로 매핑
        data_A_name = data_B_name
        data_A_follower = data_B_follower
        data_A_desc = data_B_desc
        data_A_country = data_B_country

        # 기존 B값 새로운 B 값으로 대체
        ran_data_B = random.choice(data)
        data_B_name = ran_data_B['name'] 
        data_B_follower = ran_data_B['follower_count'] 
        data_B_desc = ran_data_B['description']
        data_B_country = ran_data_B['country']

        score += 1
    else:
        os.system('cls')
        print(logo)
        print(f"You're wrong, Your score is {score}")
        break


