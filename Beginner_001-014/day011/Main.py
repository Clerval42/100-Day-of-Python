import Art
import random
print(Art.logo)

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.
# if dealer smaller than 17 draws


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
yourHand = []
dealersHand = []
isGameOver = False


def deal_card():
    """Deal a card"""
    randCard = cards[random.randint(0, 12)]
    return randCard


def resultPrint():
    print(f"    Your final hand: {yourHand}, final score: {yourSum}")
    print(f"    Computer's final hand: {dealersHand}, final score: {dealersSum}")

    if dealersSum == 0:
        print("BLACKJACK.You lose")
    elif yourSum == 0:
        print("BLACKJACK.You win")
    elif yourSum > 21:
        print("You went over. You lose 😭")
    elif dealersSum > 21:
        print("Opponent went over. You win 😁")
    elif yourSum > dealersSum:
        print("You win 😁")
    elif yourSum < dealersSum:
        print("You lose 😭")


def calculate_score(aHand):
    if len(aHand) == 2 and sum(aHand) == 21:
        return 0
    elif sum(aHand) > 21 and 11 in aHand:
        x = 1
    return sum(aHand)


for _ in range(2):
    dealersHand.append(deal_card())
    yourHand.append(deal_card())

while not isGameOver:
    yourSum = calculate_score(yourHand)
    dealersSum = calculate_score(dealersHand)
    print(f"    Your cards: {yourHand}, current score: {yourSum}")
    print(f"    Computer's first card: {dealersHand[0]}")

    if yourSum == 0 or dealersSum == 0 or yourSum > 21:
        isGameOver = True
    else:
        hitOrStand = input("Type 'y' to get another card, type 'n' to pass: ")
        if hitOrStand == "y":
            yourHand.append(deal_card())
        elif hitOrStand == "n":
            while dealersSum < 17:
                dealersHand.append(deal_card())
            isGameOver = True
resultPrint()
