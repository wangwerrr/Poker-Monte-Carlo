from deck import Deck
from card import Card
from future import FutureCards

def hand_from_string(s, fc):
    cards = s.split()

    # create an empty deck and then add every c in cards into it
    hand = Deck()
    
    for card in cards:
        # if it is a future card ('?x'), create a placeholder for it in hand
        if card[0] == '?':
            future_card = hand.add_empty_card()
            # record this card in the FutureCards pile
            fc.add_future_card(int(card[1:]), future_card) # [1:] cauz there might be a two-digit index
        # if it is a normal card, add that to hand
        else:
            hand.add_card(Card(card[0], card[1]))        
    return hand

def read_input(file, fc):
    hands = []
    with open(file) as f:
        for line in f:
            hands.append(hand_from_string(line, fc))
    return hands
