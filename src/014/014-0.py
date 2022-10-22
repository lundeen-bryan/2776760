import random
import art
from _clear_console import clear
import game_data

# Load dictionary of cards into constant
CARDS = game_data.data
score = 0 # global variable score

# pick a random card and get values (card1)
def return_random_card():
  """Returns a random card from the dictionary

  Returns:
      list: a single list (card) with name, follower_count, description, country data
  """
  card = random.choice(CARDS)
  return card

# Ask "Who has more followers (A) or (B)?"
def compare_followers(A_followers, B_followers):
  """Return who has more followers

  Args:
      A_followers (int): # of followers
      B_followers (int): # of followers

  Returns:
      str: A or B whichever has more followers
  """
  if A_followers < B_followers:
    return "A"
  if A_followers > B_followers:
    return "B"
  if A_followers == B_followers:
    return "tie"

# Get user's pick of most followed
def get_users_pick():
  """Ask user for their pick between A/B

  Returns:
      str: user's pick or exit if Q
  """
  while True:
    print("\nWho has more followers? type (A) or (B) or (Q)uit")
    user_says = input("> ").upper().strip()
    # Entry validation
    if user_says == "A" or user_says == "B":
      return user_says
    elif user_says == "Q":
      print("Thank you for playing.")
      exit(0)
    else:
      print("You can only enter the letter A or the letter B or the letter Q to quit.")

# Compare users choice with top account
def return_winner(top_account, user_choice):
  """Returns value to show if user wins or loses

  Args:
      top_account (str): A
      user_choice (str): B

  Returns:
      str: W for winner L for loser
  """
  if top_account == user_choice:
    return "W"
  if top_account != user_choice:
    return "L" # Lose

def change_score(change):
  """Increase score global var

  Args:
      change (str): inc if increas dec if decrease
  """
  global score
  if change == "inc":
    score += 1
  else:
    score -= 1
    if score < 0:
      score = 0

# main
def main():
  global score
  card_A = return_random_card()
  name_A = card_A.get("name")
  count_A = card_A.get ("follower_count")
  desc_A = card_A.get("description")
  country_A = card_A.get ("country")
  print(f"Compare A: {name_A}, a {desc_A}, from {country_A}.")
  print(art.vs)

  card_B = return_random_card()
  name_B = card_B.get("name")
  count_B = card_B.get ("follower_count")
  desc_B = card_B.get("description")
  country_B = card_B.get ("country")
  print(f"Against B: {name_B}, a {desc_B}, from {country_B}.")
  top_account = compare_followers(count_A, count_B)
  user_choice = get_users_pick()
  result = return_winner(top_account, user_choice)
  if result == "W":
    change_score("inc")
    print(f"You're right! Current score: {score}.")
    return True
  elif result == "L":
    change_score("dec")
    print(f"{art.logo}\nSorry, that's wrong. Final score: {score}.")
    return False

clear()
# Show the logo
print(art.logo)
print("""
Welcome to the higher/lower game (celebrity edition)!

Rules:
  You will be shown two celebrities or brands and you have to choose
  who has more followers on social media.
      \n""")
main()
# User completed one game, ask if they want to play again
while input("Would you like to play again? (Y)es/(N)o > ").upper() == "Y":
  clear()
  # if they want to play call main again
  main()