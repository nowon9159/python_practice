#로직 생각해보기
# 단어를 무작위 추출
# 단어의 범위 만큼 배열에 담기
# 인풋 값을 받아서 알파벳 비교, 배열의 인덱스 값에 따라 알파벳 비교
# 알파벳이 있다면 프린트 없다면 목숨-1
# 목숨 안에 단어를 맞추면 성공 -> 모든 빈칸이 채워졌는가?
# 만약 모든 빈칸이 채워지지 않고 목숨이 0 초과라면 계속 input
# 목숨 안에 단어를 못 맞추면 실패 -> 목숨이 0일때 모든 빈칸이 채워지지 않았는가?

import random

# 단어 배열에서 아무거나 추출
words = ["book", "phone", "chair", "table", "cup", "pen", "pencil", "bag", "door", "key", "spoon"]
ran_word = random.choice(words)
len_word = len(ran_word)

mark_word = []
# 단어의 범위 만큼 언더 바 추가
for i in range(len_word):
    mark_word += "_"

print(ran_word)

life = len_word

end_of_game = False

while not end_of_game:
    # 인풋 값 받기
    input_word = input("Guess a letter: ").lower()

    # 단어 배열이랑 인풋 값이랑 비교해서 일치하면 _ 배열에 insert
    for i in range(len_word):
        if ran_word[i] == input_word:
            mark_word[i] = input_word
    
    print(mark_word)

    if mark_word.count("_") == 0 :
        end_of_game = True
        print("You Win")
