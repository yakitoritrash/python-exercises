name = input("What is your name?: ")
price = int(input("What is your bid?: $"))

bids = {}

bids[name] = price

should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n")
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
