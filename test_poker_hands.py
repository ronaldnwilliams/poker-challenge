# check_p1_win(p1_hand, p2_hand)
# check_same_suit(hand)
# compare_high_card(p1_values, p2_values)
# compare_pairs(p1_value_pairs, p2_value_pairs)
# rank_player_hand(hand)

import unittest
from poker_hands import (check_p1_win, check_same_suit, compare_high_card, 
                        compare_pairs, rank_player_hand)

class PokerHandsTestCase(unittest.TestCase):
    """Tests the functions in `poker_hands.py`"""
    def setUp(self):
        self.winning_hand = ['TD', 'JD', 'QD', 'KD', 'AD']
        self.losing_hand = ['2H', '4D', '8S', '7C', 'TH']
        self.high_values = [9, 10, 11, 12, 14]
        self.low_values = [2, 5, 4, 3, 2]
        self.winning_one_pair = [[14, 14, 13, 12, 11], [[14, 2]]]
        self.winning_two_pairs = [[14, 14, 13, 13, 11], [[14, 2],[13, 2]]]
        self.losing_one_pair = [[2, 2, 3, 4, 5], [[2, 2]]]
        self.losing_two_pairs = [[2, 2, 3, 3, 4], [[2, 2],[3, 2]]]

    """Tests the check_p1_wins function"""
    # Test that check_p1_win returns true if p1_hand > p2_hand
    def test_check_p1_win_wins(self):
        self.assertTrue(check_p1_win(self.winning_hand, self.losing_hand))

    # Test that check_p1_win returns false if p1_hand < p2_hand
    def test_check_p1_win_loses(self):
        self.assertFalse(check_p1_win(self.losing_hand, self.winning_hand))

    # Test that check_p1_win returns false if tie
    def test_check_p1_win_ties(self):
        self.assertFalse(check_p1_win(self.winning_hand, self.winning_hand))

    """Tests the same_suit function"""
    # Test that check_same_suit returns true when same suit
    def test_check_same_suit_true(self):
        self.assertTrue(check_same_suit(self.winning_hand))

    # Test that check_same_suit returns false when not same suit
    def test_check_same_suit_false(self):
        self.assertFalse(check_same_suit(self.losing_hand))

    """Tests the compare_high_card function"""
    # Test that compare_high_card returns true when player 1 wins
    def test_compare_high_card_win(self):
        self.assertTrue(compare_high_card(self.high_values, self.low_values))

    # Test that compare_high_card returns false when player 1 loses
    def test_compare_high_card_loses(self):
        self.assertFalse(compare_high_card(self.low_values, self.high_values))

    # Test that compare_high_card returns false when player 1 ties
    def test_compare_high_card_ties(self):
        self.assertFalse(compare_high_card(self.high_values, self.high_values))

    """Tests the compare_pairs function"""
    # Test that compaire_pairs returns true with one winning pair
    def test_compare_pairs_one_pair_win(self):
        self.assertTrue(compare_pairs(self.winning_one_pair, self.losing_one_pair))

    # Test that compaire_pairs returns false with one losing pair
    def test_compare_pairs_one_pair_lose(self):
        self.assertFalse(compare_pairs(self.losing_one_pair, self.winning_one_pair))

    # Test that compaire_pairs returns false with tie one pair
    def test_compare_pairs_one_pair_tie(self):
        self.assertFalse(compare_pairs(self.winning_one_pair, self.winning_one_pair))

    # Test that compaire_pairs returns true with two winning pairs
    def test_compare_pairs_two_pairs_win(self):
        self.assertTrue(compare_pairs(self.winning_two_pairs, self.losing_two_pairs))

    # Test that compaire_pairs returns false with two losing pairs
    def test_compare_pairs_two_pairs_lose(self):
        self.assertFalse(compare_pairs(self.losing_two_pairs, self.winning_two_pairs))

    # Test that compaire_pairs returns false with two same pairs
    def test_compare_pairs_two_pairs_tie(self):
        self.assertFalse(compare_pairs(self.winning_two_pairs, self.winning_two_pairs))

    """Tests the compare_pairs function"""
    # Test that returns 1 for high card
    def test_rank_player_hand_high_card(self):
        self.assertEqual([1, [2, 3, 6, 8, 11]], rank_player_hand(['2D', '3H', '6S', '8C', 'JD']))

    # Test that returns 2 for one pair
    def test_rank_player_hand_one_pair(self):
        self.assertEqual([2, [2, 2, 3, 7, 8], [[2, 2]]], rank_player_hand(['2D', '2H', '3C', '7S', '8D']))

    # Test that returns 3 for two pairs
    def test_rank_player_hand_two_pairs(self):
        self.assertEqual([3, [2, 2, 3, 3, 8], [[2, 2],[3,2]]], rank_player_hand(['2D', '2H', '3C', '3S', '8D']))

    # Test that returns 4 for three of a kind
    def test_rank_player_hand_three_of_a_kind(self):
        self.assertEqual([4, [2, 2, 2, 7, 8], [[2, 3]]], rank_player_hand(['2D', '2H', '2C', '7S', '8D']))

    # Test that returns 5 for straight
    def test_rank_player_hand_straight(self):
        self.assertEqual([5, [2, 3, 4, 5, 6]], rank_player_hand(['2D', '3H', '4S', '5C', '6D']))

    # Test that returns 6 for flush
    def test_rank_player_hand_flush(self):
        self.assertEqual([6, [2, 3, 6, 8, 11]], rank_player_hand(['2D', '3D', '6D', '8D', 'JD']))

    # Test that returns 7 for full house
    def test_rank_player_hand_full_house(self):
        self.assertEqual([7, [2, 2, 2, 7, 7], [[2, 3],[7, 2]]], rank_player_hand(['2D', '2H', '2C', '7S', '7D']))

    # Test that returns 8 for four of a kind
    def test_rank_player_hand_four_of_a_kind(self):
        self.assertEqual([8, [2, 2, 2, 2, 8], [[2, 4]]], rank_player_hand(['2D', '2H', '2C', '2S', '8D']))

    # Test that returns 9 for straight flush
    def test_rank_player_hand_straight_flush(self):
        self.assertEqual([9, [2, 3, 4, 5, 6]], rank_player_hand(['2D', '3D', '4D', '5D', '6D']))

    # Test that returns 10 for royal flush
    def test_rank_player_hand_royal_flush(self):
        self.assertEqual([10], rank_player_hand(['TD', 'JD', 'QD', 'KD', 'AD']))
    
if __name__ == '__main__':
    unittest.main()