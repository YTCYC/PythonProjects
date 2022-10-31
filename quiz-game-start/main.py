from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

# for i in range(0, len(question_data)):
#     question_bank.append(Question(question_data[i]["text"], question_data[i]["answer"]))

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    question_bank.append(Question(question_text, question_answer))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    quiz.check_answer()

# quiz.final_score()
print(f"your final score is {quiz.score} / {quiz.question_number}")
