import random
from _clear_console import clear

user_cards = []
dealer_cards = []

def main(win_amount):
  bet = get_bet(100)
  deal_hands()
  starting_cards = total_cards(list=user_cards, player="Player 1", show=True)
  print(f"Player 1 is starting with {starting_cards}.")
  if starting_cards > 21:
    win_amount = lose(bet, win_amount)
  else:
    hit_or_stand = player_move()
    if hit_or_stand == "H":
      hit_me(user_cards, True) # add another card
    elif hit_or_stand == "S":
      stand()
    card_total = total_cards(list=user_cards, player="Player 1", show=False) # show card total
    print("Player 1 has " + str(card_total))
    if card_total > 21:
      win_amount = lose(bet, win_amount)
    game_result = str(show_winner())
    if game_result == "lose":
      win_amount = lose(bet, win_amount)
    elif game_result == "win":
      win_amount = win(bet, win_amount)
    elif game_result == "tie":
      tie()
      bet = 0
  print("\n\n")
  input("Press the ENTER key to continue...")
  clear()
  return win_amount

def get_bet(max_bet):
  """returns the bet amount of the
  Args:
      max_bet (int): the maximum amount you can bet from 1- this
  Returns:
      int: the bet the user wants to make on this hand
  """
  got_bet = False
  while not got_bet:
    print("How much do you want to bet? (1-{}, or QUIT)".format(max_bet))
    bet = input("> ").upper().strip()
    if bet == "QUIT":
      quit()
    if not bet.isdecimal():
      print("You must enter a number to continue.")
      continue
    bet = int(bet)
    if 1 <= bet <= max_bet:
      got_bet == True
      return bet

def hit_me(player_list, show):
  """Ads a card to the user's list (or hand)

  Args:
      player_list (list): the list of the user
      show (boolean): True/False to show the card value as it iterates

  Returns:
      str: A new card value
  """
  deal_one = random.randint(2,11)
  player_list.append(deal_one)
  if show == True:
    print(f"Card says: {deal_one}")
    return str(deal_one)

def deal_hands():
  """ deal 2 cards to each player """
  for ea in range(2):
    hit_me(player_list=user_cards, show=False)
    hit_me(player_list=dealer_cards, show=False)

def total_cards(list, player, show):
  total = 0
  for ea in list:
    if show == True:
      print(f"{player} is dealt a {ea} ")
    total = total + ea
  return total

def stand():
  print("Player 1 stands.")
  print("Player 1 has " + str(total_cards(list=user_cards, player="Player 1", show=False)))
  dealer_move()
  print("Dealer has " + str(total_cards(list=dealer_cards, player="Dealer", show=False)))

def player_move():
  """Asks player to hit or stand on the current value

  Returns:
      str: (H)it or (S)tand
  """
  print("(H)it or (S)tand?")
  move = input("> ").upper().strip()
  return move

def dealer_move():
  while total_cards(dealer_cards, "Dealer", False) < 17:
    hit_me(dealer_cards, True)

def show_winner():
  player = sum(user_cards)
  if player <=21:
    dealer = sum(dealer_cards)
    print(f"Dealer has " + str(dealer_cards) + " (" + str(dealer) + ")")
  print(f"Player 1 has " + str(user_cards) + " (" + str(player) + ")")
  # Are either > 21?
  if player > 21:
    print("You cannot have more than 21.")
    return "lose"
  elif dealer > 21:
    print("Dealer has more than 21. Busted!")
    return "win"
  elif player > dealer:
    return "win"
  elif dealer > player:
    return "lose"
  elif dealer == player:
    if dealer != 0 or player != 0:
      print("It\'s a tie, the bet is returned to you.")
      return "tie"
  else:
    return "none."

def tie():
  cleanup()

def lose(bet_amount, win_amount):
  print("You lose. You had " + str(total_cards(list=user_cards, player="Player 1", show=False)) + " cards.")
  win_amount -= bet_amount
  cleanup()
  return win_amount

def win(bet_amount, win_amount):
  print("You win!")
  print(f"You bet {bet_amount}.")
  win_amount += (bet_amount * 2)
  print(f"Now you have a total of ${win_amount} in your account.")
  cleanup()
  return win_amount

def cleanup():
  global user_cards, dealer_cards, bet_amount, win_amount
  user_cards.clear()
  dealer_cards.clear()
  bet_amount = 0

def quit():
    print("Thank you and enjoy your stay at Blackjack Hotel & Casino!\n")
    exit(0)

win_amount = 500
bet = 0
clear()
print('''Welcome to the blackjack table!

Rules:
  Try to get as close to 21 without going over.
  The card values can be between 2 - 11.
  (T)otal to see the total count of cards you have.
  (H)it to take another card.
  (S)tand to stop taking cards.
      ''')
while win_amount > 0:
  print(f"You have a total of ${win_amount} in your account.\n")
  print("Do you want to play? (Y)es / (N)o: ")
  play_game = input("> ").upper().strip()
  if play_game == "Y":
    win_amount = main(win_amount)
  else:
    quit()
if win_amount <= 0:
  print(f"You're broke.\nThank you for playing.")
