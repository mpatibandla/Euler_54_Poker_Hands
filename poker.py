from collections import OrderedDict
from operator import itemgetter

# file read and
f = open('poker.txt')
lines = f.read()
f.close()

# strip to eliminate that extra line
rounds = lines.strip().split('\n')

# dictionaries at hand to get values from card and vice versa
value_to_card = {14: 'A', 13: 'K', 12: 'Q', 11: 'J', 10: 'T', 9: '9',
              8: '8', 7: '7', 6: '6', 5: '5', 4: '4', 3: '3', 2: '2', 1: '1'}
card_to_value = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9,
              '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, '1': 1}

# converting the hands into readable format
# splitting into card value, and suite for every hand
# with the first 10 characters of the line as player 1,
# and rest as player 2


def split_cards_suites(cards):
    card = []
    suite = []
    for i in range(len(cards)):
        if i % 2 == 0:
            card.append(cards[i])
        else:
            suite.append(cards[i])
    return [card, suite]


hands = []

for i in rounds:
    i = i.replace(" ", "")
    player1_hands = split_cards_suites(i[:10])
    player2_hands = split_cards_suites(i[10:])
    hands.append([player1_hands, player2_hands])

# print hands


def royal_flush(hand):
    card = set(hand[0])
    suite = set(hand[1])
    royal_flush_set = set(['T', 'J', 'Q', 'K', 'A'])
    if card == royal_flush_set and len(suite) == 1:
        return 10
    return 0


# print royal_flush([['T', 'J', 'Q', 'K', 'A'], ['S', 'S', 'S', 'S', 'S']])


def straight_flush(hand):
    card = hand[0]
    suite = set(hand[1])
    high_value = max_card(card)
    if value_to_card[high_value-1] in card:
        if value_to_card[high_value-2] in card:
            if value_to_card[high_value-3] in card:
                if value_to_card[high_value-4] in card:
                    if len(suite) == 1:
                        return 9
    return 0


def max_card(hand):
    card = hand[0]
    high = 0
    for i in card:
        if i == 'A':
            return 14
        elif i == 'K':
            if high <= 13:
                high = 13
        elif i == 'Q':
            if high <= 12:
                high = 12
        elif i == 'J':
            if high <= 11:
                high = 11
        elif i == 'T':
            if high <= 10:
                high = 10
        elif int(i) > high:
            high = int(i)
    return high


# print straight_flush([['Q', 'J', 'T', '9', '8'], ['S', 'S', 'S', 'S', 'S']])

# depends on the number of pairs, this works for three of a kind,
# four of a kind and full house as well
def three_four_of_a_kind_and_full_house(hand):
    card = hand[0]
    count_card = dict((i, card.count(i)) for i in card)
    count_card = OrderedDict(sorted(count_card.items(), key=itemgetter(1)))
    if count_card.values() == [1, 4]:
        return 8
    if count_card.values() == [2, 3]:
        return 7
    if 3 in count_card.values():
        return 4
    return 0


# print three_four_of_a_kind_and_full_house([['8', '8', '8', '8', '4'], ['C', 'S', 'C', 'H', 'S']])
# print three_four_of_a_kind_and_full_house([['8', '8', '8', '7', '7'], ['C', 'S', 'C', 'H', 'S']])
# print three_four_of_a_kind_and_full_house([['8', '8', '8', '2', '7'], ['C', 'S', 'C', 'H', 'S']])


def flush(hand):
    suite = hand[1]
    if len(set(suite)) == 1:
        return 6
    return 0


# print flush([['7', '2', '5', '3', 'A'], ['C', 'C', 'C', 'C', 'C']])


def straight(hand):
    card = hand[0]
    high_value = max_card(hand)
    if value_to_card[high_value - 1] in card:
        if value_to_card[high_value - 2] in card:
            if value_to_card[high_value - 3] in card:
                if value_to_card[high_value - 4] in card:
                    return 5
    return 0


# print straight([['5', '6', '7', '8', '9'], ['C', 'S', 'C', 'H', 'S']])


def pair(hand):
    card = hand[0]
    count_card = dict((i, card.count(i)) for i in card)
    count_card = OrderedDict(sorted(count_card.items(), key=itemgetter(1)))
    count_pairs = count_card.values()
    if count_pairs.count(2) == 1:
        return 2
    if count_pairs.count(2) == 2:
        return 3
    return 0


# print pair([['8', '8', 'K', '9', '4'], ['C', 'S', 'C', 'H', 'S']])
# print pair([['8', '8', '9', '9', '4'], ['C', 'S', 'C', 'H', 'S']])


def highest_pair(hand):
    card = hand[0]
    count_card = dict((i, card.count(i)) for i in card)
    count_card = OrderedDict(sorted(count_card.items(), key=itemgetter(1), reverse=True))
    highest_pair = max(count_card.iteritems(), key=itemgetter(1))[0]
    highest = 0
    if card_to_value[str(highest_pair)] > highest:
        highest = card_to_value[highest_pair]
    return highest


def main():
    player1 = 0
    for i in hands:
        player1_score = 0
        player2_score = 0

        # flag to identify if pairs exist, so that can be compared later for tie
        pair_exists = 0

        if pair(i[0]):
            player1_score = pair(i[0])
            pair_exists = 1
        if three_four_of_a_kind_and_full_house(i[0]):
            player1_score = three_four_of_a_kind_and_full_house(i[0])
            pair_exists = 1
        if straight(i[0]):
            player1_score = straight(i[0])
        if flush(i[0]):
            player1_score = flush(i[0])
        if straight_flush(i[0]):
            player1_score = straight_flush(i[0])
        if royal_flush(i[0]):
            player1_score = royal_flush(i[0])

        if pair(i[1]):
            player2_score = pair(i[1])
            pair_exists = 1
        if three_four_of_a_kind_and_full_house(i[1]):
            player2_score = three_four_of_a_kind_and_full_house(i[1])
            pair_exists = 1
        if straight(i[1]):
            player2_score = straight(i[1])
        if flush(i[1]):
            player2_score = flush(i[1])
        if straight_flush(i[1]):
            player2_score = straight_flush(i[1])
        if royal_flush(i[1]):
            player2_score = royal_flush(i[1])

        if player1_score > player2_score:
            player1 += 1

        # if both the scores are equal and pairs exist, lets compare the highest pair
        # if the highest pairs are equal, look at the highest card in the hand
        elif player1_score == player2_score:
            if pair_exists:
                if highest_pair(i[0]) > highest_pair(i[1]):
                    player1 += 1
                elif highest_pair(i[0]) == highest_pair(i[1]):
                    if max_card(i[0]) > max_card(i[1]):
                        player1 += 1
            # when there are no pairs, break the tie by looking at the highest card
            else:
                if max_card(i[0]) > max_card(i[1]):
                    player1 += 1

    print player1
    # 376


if __name__ == '__main__':
    main()
