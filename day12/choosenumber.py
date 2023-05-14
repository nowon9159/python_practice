## 숫자 맞추기 게임
# 로직
# 1. 환영합니다 표시
# 2. 1부터 100 숫자 중 하나를 고르시오 표시
# 3. 1부터 100 숫자 하나를 고르게 되면 Too high Too low 표시
# 4. 정답을 맞추면 정답을 맞췄다고 출력
# 5. 2~4 반복
# 6. 난이도 설정 가능 easy , hard easy 는 맞출 수 있는 기회가 10번 hard는 5번

import random

start_logo = """
                        _   _                         _             
  __ _ _  _ ___ ______ | |_| |_  ___   _ _ _  _ _ __ | |__  ___ _ _ 
 / _` | || / -_|_-<_-< |  _| ' \/ -_) | ' \ || | '  \| '_ \/ -_) '_|
 \__, |\_,_\___/__/__/  \__|_||_\___| |_||_\_,_|_|_|_|_.__/\___|_|  
 |___/                                                              
"""

print(start_logo)

def guess_number():
    game_level = input("Welcome Choose your game level 'easy' or 'hard' : ")
    game_life = 0
    user_number = 0
    game_number = random.randrange(1, 101)
    continue_value = True

    if game_level == "easy" :
        game_life = 10
    elif game_level == "hard" :
        game_life = 5
    else :
        print("You choose wrong level")
        continue_value = False
    
    # 반복 로직
    # 유저에게 1~100 중에 숫자를 하나 고르게 한다.
    # 랜덤 숫자와 유저의 숫자를 비교해서 > < == 의 판단을 해준다.
    # 만약 유저 > 랜덤 이면 Too high 를 출력해주고 유저에게 인풋 다시 받기 && life 하나 깎기
    
    while continue_value :
        user_number = int(input(f"Choose your number : "))
        
        if user_number > game_number :
            game_life = game_life - 1
            print(f"Your number is {user_number} , too high \n Your life is {game_life}")
        elif user_number < game_number :
            game_life = game_life - 1
            print(f"Your number is {user_number} , too low \n Your life is {game_life}")
        elif user_number == game_number :
            print(f"You got it !!")
            continue_value = False
        
        if game_life == 0 :
            print("Your life is 0, You lose")
            continue_value = False
            
guess_number()
    
    



    
    
