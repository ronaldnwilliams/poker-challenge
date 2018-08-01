# Poker hand rankings from lowest to highest
# High Card: Highest value card.
# One Pair: Two cards of the same value.
# Two Pairs: Two different pairs.
# Three of a Kind: Three cards of the same value.
# Straight: All cards are consecutive values.
# Flush: All cards of the same suit.
# Full House: Three of a kind and a pair.
# Four of a Kind: Four cards of the same value.
# Straight Flush: All cards are consecutive values of same suit.
# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
import argparse

print_mode = False

# checks for --print_mode flag. if there sets print_mode to True
parser = argparse.ArgumentParser()
parser.add_argument("--print_mode", 
                    help="turns on print mode and will show each round",
                    action="store_true")
args = parser.parse_args()
if args.print_mode:
    print_mode = True

cards = []

with open('poker.txt') as f:
    for line in f: 
        cards.append(line.strip().split(' '))
f.closed

card_values = { '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, 
            '8' : 8, '9' : 9, 'T' : 10, 'J' : 11, 'Q' : 12, 
            'K' : 13, 'A' : 14 }
card_suits = ['H', 'D', 'S', 'C']
hand_ranks = { 'high card' : 1, 'one pair' : 2, 'two pairs' : 3, 
            'three of a kind' : 4, 'straight' : 5, 'flush' : 6, 
            'full house' : 7, 'four of a kind' : 8, 'straight flush' : 9,
            'royal flush': 10 }
# these are the hand ranks that need to be compared by high card
# the rest are compared by pairs unless royal flush
compare_by_high_card = [9,6,5,1]
royal_flush_values = [10, 11, 12, 13, 14]

# checks player 1 and player 2 hands
# if player 1 wins return true. if player 2 wins return false
# if tie, try to break tie. if tie can not be broken, player 2 wins
def check_p1_win(p1_hand, p2_hand):
    p1_hand_rank = rank_player_hand(p1_hand)
    p2_hand_rank = rank_player_hand(p2_hand)
    if print_mode:
        print('p1 hand rank: {}'.format(p1_hand_rank[0]))
        print('p2 hand rank: {}'.format(p2_hand_rank[0]))

    # player 1 wins
    if p1_hand_rank[0] > p2_hand_rank[0]:
        return True
    # player 2 wins
    elif p2_hand_rank[0] > p1_hand_rank[0]:
        return False
    # else there was a tie
    # if there is no tie breaker it would be a split of the pot
    # in that case return false because Player 1 did not win
    else:
        # if royal flush tie then no tie breaker
        if p1_hand_rank[0] == 10:
            return False
        # if straight flush, flush, straight, or high card
        # compare highest cards
        elif p1_hand_rank[0] in compare_by_high_card:
            return compare_high_card(p1_hand_rank[1], p2_hand_rank[1])
        # if four of a kind, full house, three of a kind, two pairs, or one pair
        # compare pairs
        else:
            return compare_pairs(p1_hand_rank[1:3], p2_hand_rank[1:3])
        
# function to check for same suit
def check_same_suit(hand):
    suit = hand[0][1]
    for card in hand:
        if card[1] != suit:
            return False
    return True

# compares the highest cards of each player
# returns true if player 1 has highest card
# returns false if player 2 has highest card or tie
def compare_high_card(p1_values, p2_values):
    # get the differences between p1 and p2
    p1_values_diff = set(p1_values)-set(p2_values)
    p2_values_diff = set(p2_values)-set(p1_values)
    
    # if there are differences
    if len(p1_values_diff):
        # check if playter 1 has highest
        if max(p1_values_diff) > max(p2_values_diff):
            return True
        # if not return false player one lost tie
        else:
            return False
    # no tie breaker 
    # return flase because player 1 did not win
    else:
        return False

# compares the pairs of each player
# returns true if player 1 has highest pair
# returns false if player 2 has highest pair
# if tie call compare highest card function
def compare_pairs(p1_value_pairs, p2_value_pairs):
    # if only one pair
    if len(p1_value_pairs[1]) == 1:
        # check value of pair
        if p1_value_pairs[1][0][0] > p2_value_pairs[1][0][0]:
            return True
        elif p1_value_pairs[1][0][0] < p2_value_pairs[1][0][0]:
            return False
        # if value of pairs is same like both queens 
        # then check rest of cards for high card
        else:
            return compare_high_card(p1_value_pairs[0], p2_value_pairs[0])
    # if multiple pairs
    else:
        # make sure sorted 
        p1_value_pairs[1].sort()
        p2_value_pairs[1].sort()
        # compare last pair's value
        if p1_value_pairs[1][-1][0] > p2_value_pairs[1][-1][0]:
            return True
        elif p1_value_pairs[1][-1][0] < p2_value_pairs[1][-1][0]:
            return False
        # tied all pairs so get high card
        else:
            return compare_high_card(p1_value_pairs[0], p2_value_pairs[0])

# function for getting the value of a ranked hand
def rank_player_hand(hand):
    same_suit = check_same_suit(hand)
    values = []

    # get card values from hand
    for card in hand:
        values.append(card_values[card[0]])
    values.sort()

    # check royal flush
    if same_suit and values == royal_flush_values:
        if print_mode:
            print(hand)
            print('royal flush')
        return [hand_ranks['royal flush']]
    else:
        # check for consecutive values
        consecutive_values = values == list(range(min(values), max(values) + 1))
        # check for straight flush
        if same_suit and consecutive_values:
            if print_mode:
                print(hand)
                print('straight flush')
            return [hand_ranks['straight flush'], values]
        else:
            # get pairs
            pairs = []
            for value in values:
                pair = [value, values.count(value)]
                if values.count(value) > 1 and pair not in pairs:
                    pairs.append(pair)
            # check four of a kind
            if len(pairs) and pairs[0][1] == 4:
                if print_mode:
                    print(hand)
                    print('four of a kind')
                return [hand_ranks['four of a kind'], values, pairs]
            # check full house
            elif len(pairs) > 1 and (pairs[0][1] == 3 or pairs[1][1] == 3):
                if print_mode:
                    print(hand)
                    print('full house')
                return [hand_ranks['full house'], values, pairs]
            # check flush
            elif same_suit:
                if print_mode:
                    print(hand)
                    print('flush')
                return [hand_ranks['flush'], values]
            # check straight
            elif consecutive_values:
                if print_mode:
                    print(hand)
                    print('straight')
                return [hand_ranks['straight'], values]
            # check three of a kind
            elif len(pairs) == 1 and pairs[0][1] == 3:
                if print_mode:
                    print(hand)
                    print('three of a kind')
                return [hand_ranks['three of a kind'], values, pairs]
            # check two pairs
            elif len(pairs) == 2:
                if print_mode:
                    print(hand)
                    print('two pairs')
                return [hand_ranks['two pairs'], values, pairs]
            # check one pair
            elif len(pairs) == 1:
                if print_mode:
                    print(hand)
                    print('one pair')
                return [hand_ranks['one pair'], values, pairs]
            # else has to be high card
            else:
                if print_mode:
                    print(hand)
                    print('high card')
                return [hand_ranks['high card'], values]

def game():
    p1_wins = 0
    p2_wins = 0
    count = 1
    for hand in cards:
        if print_mode:
            print('Round {}: '.format(count))
        count += 1
        p1_hand = hand[0:5]
        p2_hand = hand[5:10]
        if print_mode:
            print('p1 hand: {}'.format(p1_hand))
            print('p2 hand: {}'.format(p2_hand))
        p1_won = check_p1_win(p1_hand, p2_hand)
        if p1_won:
            if print_mode:
                print('p1 won\n')
            p1_wins += 1
        # TODO: looks weird
        else:
            if print_mode:
                print('p2 won\n')
            p2_wins += 1
    if print_mode:
        print('p1 wins: {}'.format(p1_wins))
        print('p2 wins: {}'.format(p2_wins))
    else:
        print('p1 wins: {}'.format(p1_wins))
        print("""
You can rerun this program with flag --print_mode
This will print information on each round of the game
        """)

game()
