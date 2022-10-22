from _clear_console import clear
from art import logo, money
# call with clear()

print(logo)
print("Welcome to the official auction!\n")

bids = {}
done_bidding = False

def return_highest_bidder(bid_data):
  high_bid = 0
  winner = ""
  for ea_bid in bid_data:
    this_bid = bid_data[ea_bid]
    if this_bid > high_bid:
      high_bid = this_bid
      winner = ea_bid
  return f"The winner is {winner} with a bid of ${high_bid}"

while not done_bidding:
  bidder = input("Enter your name: ")
  bid_value = int(input("Enter your bid: "))
  bids[bidder] = bid_value

  more_bids = input("Are there any more that want to bid? (y/n): ").lower()
  if more_bids == "n":
    done_bidding = True
    clear()
    # calculate highest bid
    print(return_highest_bidder(bids))
    print(money)
