## 블랙잭 게임 만들기
## 로직 설명


# 1. 사용자와 딜러의 카드를 1개 씩 뽑는다. -> 랜덤한 카드 뭉치의 인덱스 값
# 카드 뭉치 배열은 [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10] A 2 3 4 5 6 7 8 9 J Q K
# 2. 카드를 한 장 더 뽑는다
# if 내 카드의 합이 21 이상인 경우 Lose OR 내 카드의 합이 상대방 카드의 합보다 작으면 Lose
# elif 내 카드의 합이 상대방 카드의 합보다 크고 AND 21 이하인 경우 Win
# elif 내 카드의 합이 상대방 카드의 합과 같다면 DRAW
# 딜러가 가진 카드의 합이 17 미만인 경우 반드시 두번째 카드를 다른 카드로 받아야 한다.

import random as ran

# 카드의 값을 리스트에 저장
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
ran_card = ran.choice(cards)

# 빈 배열 생성
diller_score = []
my_score = []
continue_value = True

# 빈 배열에 랜덤 값 넣기
first_card_diller = diller_score.append(ran_card)
second_card_diller = diller_score.append(ran_card)
first_card_my = my_score.append(ran_card)
second_card_my = my_score.append(ran_card)

# 딜러와 내 스코어 합산
sum_diller_score = sum(diller_score)
sum_my_score = sum(my_score)

# 딜러 카드 & 내 스코어 오픈
print(f"Diller's second number is : {diller_score[1]}")
print(f"Your score is {sum_my_score}")


while continue_value : 
    if sum_diller_score > 20 :
        print("You win")
        continue_value = False
    elif sum_my_score > 20 :
        print("You Lose")
        continue_value = False
    elif sum_diller_score == sum_my_score :
        print("Draw")
        continue_value = False