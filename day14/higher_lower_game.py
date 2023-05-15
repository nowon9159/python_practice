##로직
# highlowergame.com을 기반
# 어느쪽이 더 많은 인스타 팔로워 수를 가질 지 체크
# 1. 첫 시작에서 랜덤으로 A값 과 B 값을 받는다
# 2. A 값과 B 값 중 어느 값이 더 많은 지 고른다 -> input
# 3. A 값과 B 값의 인스타 팔로워 수를 비교 해 input 값이 정답이라면 스코어를 하나 얻는다.
# 3.1 정답일 시 1~3 반복하고 B 값을 A 값으로 변경
# 4. 정답이 아니라면 스코어를 잃고 최종 스코어 출력 후 게임을 초기화 한다. 




from game_data import data
from art import logo, vs
import os # os.system('clear')
import random 

continue_value = False

ran_data = random.choice(data) 
 
while not continue_value :
    os.system('clear')
    print(logo)
    print(f'Compare A: {}, a {}, from {}.')
    print(vs)
    print(f'Against B: {}, a {}, from {}.')
    user_input = input("Who has more followers? Type 'A' or 'B'")

    if user_input == 'A' :

    elif user_input == 'B':
        
    else:
        print("You have wrong answer.")
        break
