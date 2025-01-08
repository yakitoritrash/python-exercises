import random

def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
    


user_card = []
computer_card = []

for _ in range(2):
    user_card.append(deal_cards())
    computer_card.append(deal_cards())



start = input("Hey! do you want to play blackjack, type 'y' or 'n'? ")


if start == 'y':
    user1 = int(user_card[0])
    user2 = int(user_card[1])
    print(f"Your cards are: {user_card} and your score is {user1 + user2}. ")
    print(f"Computer's card: [{computer_card[0]}]")
else:
    exit





#if __name__ == "__main__":
#    main()
