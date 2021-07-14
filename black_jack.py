import random

#11 - ace
#10 - jack, queen, king
deck_of_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def take_card(hand):
    while input("Do you want to take a card?(y/n)") in ["yes", "y", "ye"]:
        hand.append(random.choice(deck_of_cards))
        print(hand)

def who_wins(p_hand, d_hand):
    if sum(p_hand) > 21:
        print("You lose!\n")
    elif sum(d_hand) > 21:
        print("You win!\n")
    elif sum(p_hand) == sum(d_hand):
        print("Draw!\n")
    elif sum(p_hand) > sum(d_hand):
        print("You win!\n")
    elif sum(p_hand) < sum(d_hand):
        print("You lose!\n")

dillers_hand = []
players_hand = []
for i in range(0, 2):
    dillers_hand.append(random.choice(deck_of_cards))
    players_hand.append(random.choice(deck_of_cards))
print("[" + "".join(str(dillers_hand[0])) + ", *]")
print(players_hand)
take_card(players_hand)
print(f"Diller's hand: {dillers_hand} = {sum(dillers_hand)}\nYour hand: {players_hand} = {sum(players_hand)}\n")
who_wins(players_hand, dillers_hand)


