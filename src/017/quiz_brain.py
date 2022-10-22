class QuizBrain:
  def __init__(self, q_list):
    self.question_number = 0
    self.question_list = q_list
    self.user_score = 0
    self.max_questions = len(self.question_list)

  def still_has_questions(self):
    if self.question_number > 0:
      if self.question_number < self.max_questions:
        print(f"Your current score: {self.user_score}/{self.max_questions}\n")
      elif self.question_number >= self.max_questions:
        print(f"\nYour final score is {self.user_score}/{self.max_questions}\n")
    return self.question_number < self.max_questions

  def next_question(self):
    current_question = self.question_list[self.question_number]
    self.question_number += 1
    return f"Q.{self.question_number}: {current_question.text}"

  def check_answer(self, user_answer):
    current_question = self.question_list[self.question_number - 1]
    correct_answer = current_question.answer
    if user_answer == correct_answer:
      self.user_score += 1
      return "Correct!"
    else:
      return "False!"
