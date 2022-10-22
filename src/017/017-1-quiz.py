from _clear_console import clear
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for key in question_data:
  question_text = key["question"]
  question_answer = key["correct_answer"]
  new_question = Question(question_text, question_answer)
  question_bank.append(new_question)

quiz = QuizBrain(question_bank)

clear()
print("Welcome to Bryan's Big Question Game!\n")
while quiz.still_has_questions():
  print(f"Answer (T)rue or (F)alse to the following question:\n{quiz.next_question()}")
  user_answer = input("> ").upper().strip()
  if user_answer == "T":
    user_answer = "True"
  if user_answer == "F":
    user_answer = "False"
  print(quiz.check_answer(user_answer))
