#!/usr/local/bin/python3

import sys
from future import FutureCards
from pinput import read_input
from deck import build_remaining_deck, Deck
from evaluate import compare_hands

# provided
def print_results(wins, n):
    for i in range(0, len(wins) - 1):
        print('Hand {} won {} / {} times'.format(i, wins[i], n))
        pass
    print('and there were {} ties'.format(wins[len(wins) - 1]))
    pass

def one_trail(hands, fc, deck):
    deck.shuffle()
    fc.future_cards_from_deck(deck)
    win_hand = hands[0]
    win_ind = 0
    win_hand_2 = Deck()
    
    for i, hand in enumerate(hands):
        flag = compare_hands(win_hand, hand)
        if flag == -1:
            win_hand = hand
            win_ind = i
        elif flag == 0:
            win_hand_2 = hand
    print(win_hand)
    # tie, return last_index+1
    if compare_hands(win_hand, win_hand_2) == 0:
        return len(hands)
    # otherwise return the winning hand's index
    return win_ind

def n_trails(n, hands, fc, deck):
    # creat list of wins: [h1_win, h2_win, h3_win, tie]
    wins = [0 for _ in range(len(hands)+1)]
    for i in range(n):
        wins[one_trail(hands, fc, deck)] += 1
    return wins

def main():
    # get count of command line arguments
    argc = len(sys.argv)
    # check user input
    assert argc == 2 or argc == 3
    # make a fc, read from file
    fc = FutureCards()
    filename = sys.argv[1]
    try:
        n = int(sys.argv[2])
    except:
        n = 10000
    # read list of hand
    hands = read_input(filename, fc)
    # build remaining deck
    deck_remain = build_remaining_deck(hands)

    # do monte carlos
    wins = n_trails(n, hands, fc, deck_remain)
    # print results
    print_results(wins, n)
    pass

if __name__ == '__main__':
    main()
