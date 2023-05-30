from art import hammer
from replit import clear

print(hammer)

auction_record = {}
biding_finshed = True


def find_highest_bidder(bid_record):
  highest_bid = 0
  winner = ""
  for bidder in bid_record:
    bid_amount = bid_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")


while biding_finshed:
  bid_name = input("What is your name?: ")
  bid_amount = int(input("Enter the bid price: $"))
  auction_record[bid_name] = bid_amount
  continue_bid = input(
    "Type 'yes' for other user to bid, else 'no':\n").lower()
  if continue_bid == "no":
    biding_finshed = False
    find_highest_bidder(auction_record)
  elif continue_bid == "yes":
    clear()
