import unittest
import poker


class TestPoker(unittest.TestCase):

    def test_royal_flush(self):
        hand1 = poker.royal_flush([['T', 'J', 'Q', 'K', 'A'], ['S', 'S', 'S', 'S', 'S']])
        self.assertEqual(hand1, 10)
        hand2 = poker.royal_flush([['T', 'T', 'Q', 'K', 'A'], ['S', 'D', 'S', 'C', 'S']])
        self.assertEqual(hand2, 0)

    def test_check_straightflush(self):
        hand1 = poker.straight_flush([['Q', 'J', 'T', '9', '8'], ['S', 'S', 'S', 'S', 'S']])
        self.assertEqual(hand1, 9)
        hand2 = poker.straight_flush([['A', 'J', '1', '4', '8'], ['D', 'S', 'H', 'S', 'S']])
        self.assertEqual(hand2, 0)

    def test_check_flush(self):
        hand1 = poker.flush([['7', '2', '5', '3', 'A'], ['C', 'C', 'C', 'C', 'C']])
        self.assertEqual(hand1, 6)
        hand2 = poker.flush([['7', '2', '5', '3', 'A'], ['D', 'H', 'C', 'C', 'C']])
        self.assertEqual(hand2, 0)

    def test_check_straight(self):
        hand1 = poker.straight([['5', '6', '7', '8', '9'], ['C', 'S', 'C', 'H', 'S']])
        self.assertEqual(hand1, 5)
        hand2 = poker.straight([['A', '6', 'T', '8', '9'], ['C', 'S', 'C', 'H', 'D']])
        self.assertEqual(hand2, 0)

    def test_four_of_a_kind(self):
        hand1 = poker.three_four_of_a_kind_and_full_house([['8', '8', '8', '8', '4'], ['C', 'S', 'C', 'H', 'S']])
        self.assertEqual(hand1, 8)
        hand2 = poker.three_four_of_a_kind_and_full_house([['8', '6', '8', '8', '4'], ['C', 'S', 'C', 'H', 'S']])
        self.assertEqual(hand2, 4)

    def test_full_house(self):
        hand1 = poker.three_four_of_a_kind_and_full_house([['8', '8', '8', '7', '7'], ['C', 'S', 'C', 'H', 'S']])
        self.assertEqual(hand1, 7)
        hand2 = poker.three_four_of_a_kind_and_full_house([['1', '8', '8', '7', '7'], ['C', 'S', 'C', 'H', 'S']])
        self.assertEqual(hand2, 0)

    def test_three_of_a_kind(self):
        hand1 = poker.three_four_of_a_kind_and_full_house([['8', '8', '8', '2', '7'], ['C', 'S', 'C', 'H', 'S']])
        self.assertEqual(hand1, 4)
        hand2 = poker.three_four_of_a_kind_and_full_house([['8', '1', '8', '2', '7'], ['C', 'S', 'C', 'H', 'S']])
        self.assertEqual(hand2, 0)

    def test_two_pair(self):
        hand1 = poker.pair([['8', '8', '9', '9', '4'], ['C', 'S', 'C', 'H', 'S']])
        self.assertEqual(hand1-1, 2)
        hand2 = poker.pair([['1', '1', '8', '8', '4'], ['C', 'S', 'C', 'H', 'S']])
        self.assertEqual(hand2-1, 2)
        hand3 = poker.pair([['1', '8', '8', '7', '7'], ['C', 'S', 'C', 'H', 'S']])
        self.assertEqual(hand3-1, 2)

    def test_one_pair(self):
        hand1 = poker.pair([['8', '8', 'A', '9', '4'], ['C', 'S', 'C', 'H', 'S']])
        self.assertEqual(hand1-1, 1)
        hand2 = poker.pair([['8', '1', 'A', '9', '4'], ['C', 'S', 'C', 'H', 'S']])
        self.assertEqual(hand2, 0)

    def test_highest_card(self):
        hand1 = poker.max_card([['8', '8', '9', '9', '4'], ['C', 'S', 'C', 'H', 'S']])
        hand2 = poker.max_card([['Q', 'J', 'T', '9', '8'], ['S', 'S', 'S', 'S', 'S']])
        self.assertEqual(hand1, 9)
        self.assertEqual(hand2, 12)


if __name__ == '__main__':
    unittest.main()
