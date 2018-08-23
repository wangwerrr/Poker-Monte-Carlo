from card import Card, card_from_num
import random

class Deck:
    """a list of card"""
    def __init__(self):
        self.cards = []
        
    def __str__(self):
        return ' '.join([str(c) for c in self.cards])
    
    def __repr__(self):
        return 'Deck(' + ' '.join([str(c) for c in self.cards]) + ')'
        
    def add_card(self, c):
        self.cards.append(c)
        
    def add_empty_card(self):
        default = Card()
        self.cards.append(default)
        return default
        
    def contains(self, c):
        for card_in_deck in self.cards:
            if card_in_deck == c:
                return True
        return False
    
    def shuffle(self):
        random.shuffle(self.cards)
        
    def assert_full(self):
        for i in range(52):
            assert self.contains(card_from_num(i)) 
    
    # takes card from from deck, appends it to end, and returns it
    def draw(self):
        self.cards.append(self.cards[0])
        return self.cards.pop(0)
        
    # sorts high to low
    def sort(self):
        self.cards.sort(reverse=True)

# builds and returns complete deck except for cards in hands
def build_remaining_deck(hands):
    # creat a full deck
    deckRemain = Deck()
    for i in range(52):
        c = card_from_num(i)
        flag = 0
        # check if there's any hand that contains this card
        for hand in hands:
            if hand.contains(c) == True: flag = 1
        # if no hands have c, add c to the deck
        if flag == 0:
            deckRemain.add_card(c)
    return deckRemain

