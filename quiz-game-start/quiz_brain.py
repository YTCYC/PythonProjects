class QuizBrain:
    def __init__(self, q_list):
        # question_number = 0
        self.question_number = 0
        self.score = 0
        self.user_answer = ""
        self.question_answer = ""
        self.question_list = q_list

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_answer = question.answer
        self.question_number += 1
        self.user_answer = input(f"Q.{self.question_number}: {question.text}. (True/False?) ")

    def still_has_questions(self):
        return self.question_number <= len(self.question_list) - 1
        #     return True
        # else:
        #     return False

    def check_answer(self):
        if self.user_answer.lower() == self.question_answer.lower():
            self.score += 1
            print("You got it right")
        else:
            print("Wrong answer")
        print(f"you current score is {self.score} / {self.question_number}")
        print("\n")

    def final_score(self):
        print(f"your final score is {self.score} / {self.question_number}")
