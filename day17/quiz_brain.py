# asking the questions
# checking if the answer was correct
# checking if we're the end of the quiz

# Create a class called QuizBrain
class QuizBrain:
    # Write an __init() method
    # Initilalise the question_number to 0
    # Initialise the question_list to an input.
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
            
    # Retrieve the item at the current question_number from the question_list.
    # Use the input() function to show the Question text and ask for the user's answer
    def next_question(self):
        current_question = self.question_list[self.question_number] # 한 클래스 내에서 선언한 속성은 . 을 통해 다른 메소드에서도 불러올 수 있다.
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        # 정답 비교하고 스코어 올리기
        if user_answer.lower() == correct_answer.lower() : 
            self.score += 1
            print("You got it right!")
        else :
            print("That's Wrong.")

        # 리스트 length 만큼 반복하기
        if self.question_number < len(self.question_list) :
            print(f"The correct answer was: {correct_answer}.")
            print(f"Your current score is : {self.score}/{self.question_number}.")
            print("\n")
            
        # 마지막 질문일 경우 다른 문자열 출력
        elif self.question_number == len(self.question_list) :
            print("You've completed the quiz")
            print(f"Your final score was: {self.score}/{len(self.question_list)}")
            


