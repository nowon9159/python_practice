## 숫자 맞추기 게임
# 로직
# 1. 환영합니다 표시
# 2. 1부터 100 숫자 중 하나를 고르시오 표시
# 3. 1부터 100 숫자 하나를 고르게 되면 Too high Too low 표시
# 4. 정답을 맞추면 정답을 맞췄다고 출력
# 5. 2~4 반복
# 6. 반복 시 난이도 설정 가능 easy , hard easy 는 맞출 수 있는 기회가 10번 hard는 5번


start_logo = """
                        _   _                         _             
  __ _ _  _ ___ ______ | |_| |_  ___   _ _ _  _ _ __ | |__  ___ _ _ 
 / _` | || / -_|_-<_-< |  _| ' \/ -_) | ' \ || | '  \| '_ \/ -_) '_|
 \__, |\_,_\___/__/__/  \__|_||_\___| |_||_\_,_|_|_|_|_.__/\___|_|  
 |___/                                                              
"""

print(start_logo)

continue_value = True
game_level = input("Welcome Choose your game level 'easy' or 'hard'")
game_life = 0

if game_level == "easy" :
    game_life = 10
elif game_level == "hard" :
    game_life = 5
else :
    print("You choose wrong level")
    game_level = input("Choose your game level 'easy' or 'hard'")

def guess_number():
    while continue_value :
        
        return False



guess_number()