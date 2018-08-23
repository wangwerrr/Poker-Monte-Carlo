from deck import Deck
from card import Card

class FutureCards:
    """ Class Future Cards"""
    def __init__(self):
        self.future_cards = []

    def __str__(self):
        # ??? don't know if it follows the instruction
        return '\n'.join([str(d) for d in self.future_cards])
    
    def __repr__(self):
        lines = [] 
        for i, d in enumerate(self.future_cards):
            l = '?{}: {}'.format(i, str(d))
            lines.append(l)
        return 'FutureCards:\n' + '\n'.join(lines)  
        
    def add_future_card(self, ind, c):
        L = len(self.future_cards)
        if ind < L:
            pass
        else:
            for _ in range(ind-L+1):
                self.future_cards.append(Deck())
        self.future_cards[ind].add_card(c)
    
    def future_cards_from_deck(self, d):
        for deck_to_be_filled in self.future_cards:
            card = d.draw()
            cards = deck_to_be_filled.cards
            for c in cards:
                c.value = card.value
                c.suit = card.suit
            """
            for i in range(len(deck_to_be_filled.cards)):

                deck_to_be_filled.cards[i].value = c.value
                deck_to_be_filled.cards[i].suit = c.suit
            """     

