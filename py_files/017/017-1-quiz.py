from tkinter import TclError
from _clear_console import clear
from question_model import Question
from data import question_data

question_bank = []
for key in question_data:
  question_text = key.get("text")
  question_answer = key.get("answer")
  new_question = Question(question_text, question_answer)
  question_bank.append(new_question)


print(question_bank[0].text)