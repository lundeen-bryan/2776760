import random
from hangman_art import stages
from hangman_art import logo
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_len = len(chosen_word)
game_over = False
lives = 6 #user starts w/6 lives

print(logo)
print(f"the chosen word is {chosen_word}\n") #temporarily use hint for debugging

#create blank lines
display = []
for _ in range(word_len):
  display += "_"

print(stages[lives])

#get user input loop til game over
while not game_over:
  guess = input("Guess a letter: ").lower()

  if guess in display:
    print(f"You've already guessed the letter {guess}.")

  #check user input for match
  for position in range(word_len):
    letter = chosen_word[position]
    #print(f"Current position: {position} \nCurrent letter: {letter} \nGuessed letter: {guess}")

    if letter == guess:
      display[position] = letter

  if guess not in chosen_word:
    print(f"You guessed {guess}, that's not in the word. You lose a life.")
    lives -= 1
    if lives == 0:
      game_over = True
      print("\nGame Over.\nYou lose.")
    else:
      print(f"Lives remaining: {lives}")

  #join elements in list; convert to string
  print(f"{' '.join(display)}")

  #if there are no more letters to guess game over
  if "_" not in display:
    game_over = True
    print("You Win!")

  print(stages[lives])
