## O/X 게임 만들기
## 로직
# 1. 질문 클래스 만들기
# 2. 

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
# Write a for loop to iterate over the question_data.
# Create a Question object from each entry in question_data.
# Append each Question object to the question_bank

question_bank = []

for i in question_data:
    question = i["question"]
    answer = i["correct_answer"]
    new_q = Question(question, answer)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions() :
    quiz.next_question()