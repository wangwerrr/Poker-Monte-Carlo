import random

# constants for card values ACE, KING, etc.
ACE, KING, QUEEN, JACK = 14, 13, 12, 11
valueSet =  set(['2','3','4','5','6','7','8','9','0','J','Q','K','A','?'])
suitSet = set(['s','h','d','c','?'])


def value_from_letter(let):
    if let in valueSet:        
        if let == 'A':
            return 14
        elif let == 'K':
            return 13
        elif let == 'Q':
            return 12
        elif let == 'J':
            return 11
        elif let == '0':
            return 10
        elif let == '?':
            return 0
        else:
            return int(let)
    else:
        raise ValueError('invalid Card value: {}'.format(let))

def check_suit(let):
    if let in suitSet:
        return let
    else:
        raise ValueError('invalid Card suit: {}'.format(let))

def num_to_suit(num):
    numDict = {0:'c', 1:'d', 2:'h', 3:'s'}
    try:
        return numDict[num]
    except:
        return '?'

def suit_to_num(suit):
    suitDict = {'c':0, 'd':1, 'h':2, 's':3}
    return suitDict[suit]
    
def letter_from_value(val):
    if val == 14:
        return 'A'
    elif val == 13:
        return 'K'
    elif val == 12:
        return 'Q'
    elif val == 11:
        return 'J'
    elif val == 10:
        return '0'
    elif val == 0:
        return '?'
    else:
        return str(val)

def is_valid_value(value):
    # convert num to letter before judging
    if letter_from_value(value) not in valueSet:
        return False
    else:
        return True

def is_valid_suit(suit):
    if suit not in suitSet:
        return False
    else:
        return True

class Card:
    """A class to represent a card with a value and suit"""
    def __init__(self, value_let = '?', suit_let = '?'):
        self.value = value_from_letter(value_let)
        
        self.suit = check_suit(suit_let)

    def __str__(self):        
        if is_valid_value(self.value) == True and is_valid_suit(self.suit) == True:
            return '{}{}'.format(letter_from_value(self.value), self.suit)
        else:
            raise ValueError('invalid Card')
    
    def __repr__(self):
        if is_valid_value(self.value) == True and is_valid_suit(self.suit) == True:
            return 'Card({}{})'.format(letter_from_value(self.value), self.suit)
        else:
            raise ValueError('invalid Card')

    def __eq__(self, other):
        if self.value == other.value and self.suit == other.suit:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.value != other.value:
            return self.value < other.value
        else:
            return suit_to_num(self.suit) < suit_to_num(other.suit)
        
    def is_valid(self):
        # valid if only in valueset AND  known
        if is_valid_value(self.value) and is_valid_suit(self.suit) and self.value != 0 and self.suit != '?':
            return True
        else:
            return False

def card_from_num(num):
    pick_value = num % 13 + 2
    pick_suit = num_to_suit(num // 13)
    c = Card()
    c.value = pick_value
    c.suit = pick_suit
    # how to use is_valid()?
    if c.is_valid():
        return c
    else:
        raise ValueError('invalid input number')
