#로직 생각해보기
# 단어를 무작위 추출
# 단어의 범위 만큼 배열에 담기
# 인풋 값을 받아서 알파벳 비교, 배열의 인덱스 값에 따라 알파벳 비교
# 알파벳이 있다면 프린트 없다면 목숨-1
# 목숨 안에 단어를 맞추면 성공 -> 모든 빈칸이 채워졌는가?
# 목숨 안에 단어를 못 맞추면 실패 -> 목숨이 0일때 모든 빈칸이 채워지지 않았는가?

import random

# 단어 배열에서 아무거나 추출
words = ["book", "phone", "chair", "table", "cup", "pen", "pencil", "bag", "door", "key"]
ran_word = random.choice(words)

# 단어의 범위 만큼 다시 배열에 담기
selected_word = []
for i in range(0,len(ran_word)):
    selected_word.append(ran_word[i])

# 인풋 값 받기
print(ran_word)
guess_word = input("Guess a letter : ")

# 유저 인풋 값 확인해서 선택된 배열의 값과 비교
for i in range(0,len(ran_word)):
    if guess_word == selected_word[i] :
        print("Right")
    else:
        print("Wrong")


