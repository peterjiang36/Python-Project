logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")


bid_dictionary = {}

continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    bid_price = int(input("What is your bid price?: $"))
    bid_dictionary[name] = bid_price
    other_bid = input("Are there any other people want to bid? Type 'yes' or 'no'. \n").lower()
    if other_bid == "no":
        continue_bidding = False
        find_highest_bidder(bid_dictionary)
    else:
        print("\n" * 100)
