import random
from art import logo
from _clear_console import clear

# Using constants not global variables
LOWER_NUM = 1 # Lowest number in range
UPPER_NUM = 100 # Highest number in range
EASY_LEVEL = 10 # Number of attempts for easy
HARD_LEVEL = 5 # Number of attempts for hard

def set_difficulty():
  """Let user choose the difficulty of the game & this sets # of attempts

  Returns:
      string: easy or hard from constants above
  """
  while True:
    print("Choose a difficulty. (E)asy or (H)ard")
    difficulty = input("> ").upper().strip()
    if difficulty == "H":
      print("You have chosen the hard level.")
      return HARD_LEVEL
    elif difficulty == "E":
      print("You have chosen the easy level.")
      return EASY_LEVEL
    else:
      print("Your choice must be either E or H to continue...")
      continue

def return_random_number():
  """ Pick a random number for the game

  Returns:
      int: number between constants LOWER_NUM, UPPER_NUM
  """
  return random.randint(LOWER_NUM, UPPER_NUM)

def return_attempt_number(current_attempt):
  """Returns number of attempts minus one

  Args:
      current_attempt (int): the current attempt number

  Returns:
      int: new number
  """
  current_attempt -= 1
  return current_attempt

def check_guess(winning_number, user_guess):
  """Returns a hint to user or calls win depending on arg

  Args:
      winning_number (int): the number that was randomly picked by computer
      user_guess (int): the number the user guessed

  Returns:
      string or int: if wrong guess returns str msg, else sends winning_number to win
  """
  if user_guess < winning_number:
    return f"{user_guess} is too low.\nGuess again."
  elif user_guess > winning_number:
    return f"{user_guess} is too high.\nGuess again."
  else:
    return "win"

def win(guess):
  """Returns msg to let user know they won

  Args:
      guess (int): the number user guessed

  Returns:
      string: msg to let user know they won
  """
  return f"Winner! Winner! Chicken Dinner!\n{guess} is correct!."

def main():
  # Loop until user runs out of guesses or is correct
  keep_asking = True
  # Ask user if they way easy/hard level and set # of attempts available
  attempts = set_difficulty()
  # Set the winning number user needs to guess
  winning_number = return_random_number()
  # Code above not needed anymore just loop below until done
  while keep_asking:
    # Keep asking user for a number
    while True:
      # Use upper/lower constants for guess range
      print(f"Guess a number between {LOWER_NUM} and {UPPER_NUM}:")
      # prompt user for number input
      guess = input("> ").strip()
      # Check if user entered number, if not ask again
      if str.isnumeric(guess):
        # User entered number
        break
      else:
        # User didn't enter a number, loop again
        continue
    # User entered a number, check against winning number
    check = check_guess(int(winning_number), int(guess))
    # If the return is not string "win"
    if check != "win":
      # Give user a hint
      print(check)
      # See how many attempts are left
      attempts = return_attempt_number(attempts)
      # User loses if no attempts left
      if attempts == 0:
        print("Sorry. You have no more attempts left to guess. Thank you for playing.")
        keep_asking = False
        return keep_asking
      # Else show user how many more guesses they have left
      else:
        print(f"You have {attempts} attempts remaining to guess the number.")
    # If the guess matched the winning number
    elif check == "win":
      # Tell user they won and exit main
      winning_msg = win(guess)
      print(winning_msg)
      keep_asking = False
      return False

# load the logo
clear()
print(logo)

# welcome player
print("Welcome to the Number Guessing Game!")

main()
# User completed one game, ask if they want to play again
while input("Would you like to play again? (Y)es/(N)o > ") == "Y":
  clear()
  # if they want to play call main again
  main()
