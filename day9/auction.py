def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount    
            winner = bidder
    
    print("The winner is {winner} with a bid of {highest_bid}")

bids = {}



continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)
        



    

# more = input("Do we have any more bidders?")

# if more == "no":
#     values = {}
#     for value in values:
#         values += [name]
        
#     print(values)


# elif more == "yes":
#     print(" \n"*100)
#     name = input("What is your name?")
#     bid = input("How much do you wanna bid?")
#     more = input("Do we have any more bidders?")
