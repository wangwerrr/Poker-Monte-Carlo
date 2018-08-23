Now you are ready to put the whole program together! You have the file
poker.py, which you will use to do the simulations.

In particular, your program should take one or two command line
arguments. The first is required and is the name of the input file to
read. The second is optional and is the number of Monte Carlo trials
to perform. If it is not given, you should use 10,000 as a default
value.

Your main poker.py should:
  - Check command line arguments/report errors.
  - Make a FutureCards and make hands from read_input, passing in the
    filename. 
  - Create a deck with the remaining cards (you just wrote
    build_remaining_deck).
  - Create a list wins to count how many times each hand wins, with
    one more element for if there was a tie (so if there are two
    hands, you should have three elements). Initialize all its values
    to 0. 
  - Do each Monte Carlo trial (repeat num_trials times). Hint: you
    want to abstract this out into a function! 
      o Shuffle the deck of remaining cards
      o Assign unknown cards from the shuffled deck (you just wrote
        future_cards_from_deck)
      o Use compare_hands (from eval.py) to figure out which hand
        won. Note that with potentially more than two hands, this is
	much like finding the max of an array but using compare_hands
	instead of >. If two hands tie, you will need to keep track of
	the second one to compare the best and second best option at
	the end.
      o Increment the win count for the winning hand (or for the
        "ties" element of the list if there was a tie).
  - After you do all your trials, you just need to print your results
    (we provide print_results), as Python will automatically
    deallocate memory and close open files.
