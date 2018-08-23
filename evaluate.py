from card import Card, card_from_num, ACE, KING, QUEEN, JACK
from deck import Deck
import operator

# finds flush su
def find_flush(hand):
    suitOccur = {'s': 0, 'c': 0, 'h': 0, 'd':0}

    for card in hand.cards:   
        if card.is_valid():
            suitOccur[card.suit] += 1
    if suitOccur['s'] >= 5:
        return 's'
    elif suitOccur['c'] >=5:
        return 'c'
    elif suitOccur['h'] >=5:
        return 'h'
    elif suitOccur['d'] >= 5:
        return 'd'
    else:
        return None
        
# makes dictionary of cards values to count of their occurances
def count_values(hand):
    valueOccur = {}

    for card in hand.cards:
        if card.is_valid():
            value = card.value
            if value in valueOccur:
                valueOccur[value] += 1
            else:
                valueOccur[value] = 1
    return valueOccur # ordered dict??????
        
# uses counts dict and returns a tuple (value with most n of a kind, n)
def dict_to_ordered_tuple_list(dic):
    # convert the dict it into tuple (value, count)
    lst = dic.items()
    # sort by count x[1], then by value x[0], both from high to low
    return sorted(lst, key=lambda x: (x[1],x[0]), reverse=True)

def get_max_count(hand, counts):
    # where should i use hand???
    counts = dict_to_ordered_tuple_list(counts)
    return counts[0] # (value, count)
    
# finds index of second pair or returns -1 for no sec pair
def find_secondary_pair(hand, counts, val):
    counts = dict_to_ordered_tuple_list(counts)
    for value,count in counts:
        # if there is a second pair, note count should be >=2 cuz eg. AAA KKK QQ, we should select KK as the second pair
        if count >= 2 and value != val:
            # find the index of the second pair in hand
 
            for index, card in enumerate(hand.cards):
                if card.value == value:
                    return index
    return -1
                    
# get first index of value in hand
def get_kind_index(hand, value):
    for index, card in enumerate(hand.cards):
        if card.value == value:
            return index
    return -1

# build hand with n of a kind starting at ind
def build_of_a_kind(hand, n, ind):
    n_of_a_kind = Deck()
    for key_card in hand.cards[ind:ind+n]:
        n_of_a_kind.add_card(key_card) 
    num_remain = 5 - len(n_of_a_kind.cards)
    
    for card in hand.cards:
        if num_remain == 0:
            break
        if card.value != n_of_a_kind.cards[0].value:
            n_of_a_kind.add_card(card)
            num_remain -= 1
    return n_of_a_kind
# adds secondary pair (for full house or two pair)
def add_pair(hand, pi, ans, ai):
    # hand : 8 cards
    # pi: second pair index in hand
    # ans: could be 3 of a kind or one pair + remains; should replace remains with the second pair and rebuild the remains
    # ai: index of ans to put the second pair
    new_deck = Deck()
    for i in range(ai):
        new_deck.add_card(ans.cards[i])
    ans = new_deck
    ans.add_card(hand.cards[pi])
    ans.add_card(hand.cards[pi+1])
    if ai == 2:
        skip_values = [ans.cards[0].value, hand.cards[pi].value]
        # and one more card with the highest value in hand:
        for card in hand.cards:
            if card.value not in skip_values:
                ans.add_card(card)
                break
    return ans

# helper for is_straight_at
def is_n_length_straight_at(hand, ind, fs, n):
    # A K Q J 0
    # ind is the start of a straight
    if fs != None:
        fs_suit_deck = Deck()
        for card in hand.cards:
            if card.suit == fs:
                fs_suit_deck.add_card(card)
        hand = fs_suit_deck
        
    firstCard = hand.cards[ind]
    curValue = firstCard.value    
    endValue = curValue - n + 1

    curValue -= 1
    curIndex = ind+1

    for card in hand.cards[ind+1:]:
        if curValue < endValue:
            break
        if card.value == curValue:
            curValue -= 1
        curIndex += 1

    if curValue == endValue - 1:
        return True
    else:
        return False
    
# helper for is_straight_at
def is_ace_low_straight_at(hand, ind, fs):
    # a straight of length 4 + A
    if fs != None:
        fs_suit_deck = Deck()
        for card in hand.cards:
            if card.suit == fs:
                fs_suit_deck.add_card(card)
        hand = fs_suit_deck

    exist_5 = False
    for i in range(len(hand.cards)):
        if hand.cards[i].value == 5:
            ind_for_value_5 = i
            exist_5 = True
            break
        
    if exist_5 and hand.cards[0].value == ACE and is_n_length_straight_at(hand, ind_for_value_5, fs, 4):
        return True
    else:
        return False
            
# if fs = None, look for any straight
# if fs = suit, look for straight in suit
# returns -1 for ace-low, 1 for straight, 0 for no straight
def is_straight_at(hand, ind, fs):
    # ind: then index where the potential straight starts from
    # fs: flush suit eg 's'
    if is_n_length_straight_at(hand, ind, fs, 5): return 1
    elif is_ace_low_straight_at(hand, ind, fs): return -1
    else: return 0
            
# provided
def copy_straight(hand, ind, fs, ace_low=False):
    ans = Deck()
    last_card = None
    target_len = 5
    assert not fs or hand.cards[ind].suit == fs
    if ace_low:
        assert hand.cards[ind].value == ACE
        last_card = hand.cards[ind]
        target_len = 4
        to_find = 5
        ind += 1
        pass
    else:
        # regular straight
        to_find = hand.cards[ind].value
        pass
    while len(ans.cards) < target_len:
        assert ind < len(hand.cards)
        if hand.cards[ind].value == to_find:
            if not fs or hand.cards[ind].suit == fs:
                ans.add_card(hand.cards[ind])
                to_find -= 1
                pass
            pass
        ind += 1
        pass
    if last_card is not None:
        ans.add_card(last_card)
        pass
    assert len(ans.cards) == 5
    return ans

# provided
# looks for a straight (or straight flush if fs is not None)
# calls the student's is_straight_at for each index
# if found, copy_straight returns cards used for straight
def find_straight(hand, fs):
    for i in range(0, len(hand.cards) - 4):
        is_straight = is_straight_at(hand, i, fs)
        if is_straight == 1:
            # straight
            return copy_straight(hand, i, fs)
        pass
    for i in range(0, len(hand.cards) - 4):
        is_straight = is_straight_at(hand, i, fs)
        if is_straight == -1:
            # ace-low straight
            return copy_straight(hand, i, fs, True)
        pass
    return None

# provided
# builds hand with flush suit fs
def build_flush(hand, fs):
    ans = Deck()
    i = 0
    while len(ans.cards) < 5:
        assert i < len(hand.cards)
        if hand.cards[i].suit == fs:
            ans.add_card(hand.cards[i])
            pass
        i += 1
        pass
    return ans

# provided
def evaluate_hand(hand):
    # straight flush
    fs = find_flush(hand)
    straight = find_straight(hand, fs)
    if fs and straight:
        return straight, 'straight flush'
    # four of a kind
    val_counts = count_values(hand)
    v, n = get_max_count(hand, val_counts)
    assert n <= 4
    ind = get_kind_index(hand, v)
    if n == 4:
        return build_of_a_kind(hand, 4, ind), 'four of a kind'
    # full house
    sec_pair = find_secondary_pair(hand, val_counts, v)
    if n == 3 and sec_pair >= 0:
        ans = build_of_a_kind(hand, 3, ind)
        ans = add_pair(hand, sec_pair, ans, 3)
        return ans, 'full house'
    # flush
    if fs:
        return build_flush(hand, fs), 'flush'
    # straight
    if straight:
        return straight, 'straight'
    # three of a kind
    if n == 3:
        return build_of_a_kind(hand, 3, ind), 'three of a kind'
    # two pair
    if n == 2 and sec_pair >=0:
        ans = build_of_a_kind(hand, 2, ind)
        ans = add_pair(hand, sec_pair, ans, 2)
        return ans, 'two pair'
    # pair
    if n == 2:
        return build_of_a_kind(hand, 2, ind), 'pair'
    # high card
    ans = Deck()
    ans.cards = hand.cards[0:5]
    return ans, 'high card'

def num_from_rank(r):
    ranks = ['high card', 'pair', 'two pair', 'three of a kind', \
                 'straight', 'flush', 'full house', \
                 'four of a kind', 'straight flush']
    return ranks.index(r)

# returns positive if hand1 > hand2, 
# 0 for tie, or 
# negative for hand2 > hand 1
def compare_hands(hand1, hand2):
    # return (5 card hand, rank)
    hand1.sort()
    hand2.sort()
    
    ans1 = evaluate_hand(hand1)
    ans2 = evaluate_hand(hand2)

    final_hand1 = ans1[0]
    final_hand2 = ans2[0]
    r1 = num_from_rank(ans1[1])
    r2 = num_from_rank(ans2[1])

    if r1 > r2:
        return 1
    elif r1 < r2:
        return -1
    else:
        # compare value in final hand
        return compare_value(final_hand1, final_hand2)
      
def compare_value(hand1, hand2):
    # which highest value is bigger
    for c1, c2 in zip(hand1.cards, hand2.cards):
        if c1.value > c2.value:
            return 1
        elif c1.value < c2.value:
            return -1
    return 0
