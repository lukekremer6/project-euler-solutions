from collections import Counter

def check_straight_flush(hand):
    cards, has_straight = check_straight(hand)
    _, has_flush = check_flush(hand)
    result = has_straight and has_flush
    if not result:
        cards = []
    return cards, result

def check_straight(hand):
    result = False

    # Try counting Ace as 14
    i = hand[0][0]
    for card in hand[1:]:
        i += 1
        if i != card[0]:
            break
    else:
        result = True

    # Try counting Ace as 1
    for i in range(len(hand)):
        if hand[i][0] == 14:
            hand[i][0] = 1
    hand.sort()
    i = hand[0][0]
    for card in hand[1:]:
        i += 1
        if i != card[0]:
            break
    else:
        result = True
    
    if result:
        cards = sorted([card[0] for card in hand], reverse=True)
    else:
        # Reset Ace to 14
        for i in range(len(hand)):
            if hand[i][0] == 1:
                hand[i][0] = 14
        cards = []
    return cards, result

def check_flush(hand):
    result = all(hand[0][1] == card[1] for card in hand[1:])
    if result:
        cards = sorted([card[0] for card in hand], reverse=True)
    else:
        cards = []
    return cards, result

def check_full_house(hand):
    cards, has_three_of_a_kind = check_three_of_a_kind(hand)
    _, has_one_pair = check_one_pair(hand)
    result = has_three_of_a_kind and has_one_pair
    if not result:
        cards = []
    return cards, result

def check_four_of_a_kind(hand):
    count = Counter(card[0] for card in hand)
    main_card = -1
    result = False
    for key, value in count.items():
        if value == 4:
            result = True
            main_card = key
    if result:
        cards = [main_card] * 4 + sorted([card[0] for card in hand if card[0] != main_card], reverse=True)
    else:
        cards = []
    return cards, result

def check_three_of_a_kind(hand):
    count = Counter(card[0] for card in hand)
    main_card = -1
    result = False
    for key, value in count.items():
        if value == 3:
            result = True
            main_card = key
    if result:
        cards = [main_card] * 3 + sorted([card[0] for card in hand if card[0] != main_card], reverse=True)
    else:
        cards = []
    return cards, result

def check_two_pair(hand):
    count = Counter(card[0] for card in hand)
    main_cards = []
    for key, value in count.items():
        if value == 2:
            main_cards.append(key)
    result = len(main_cards) == 2
    if result:
        main_cards.sort(reverse=True)
        cards = main_cards[:1] * 2 + main_cards[1:] * 2 + [card[0] for card in hand if card[0] not in main_cards]
    else:
        cards = []
    return cards, result

def check_one_pair(hand):
    count = Counter(card[0] for card in hand)
    main_cards = []
    for key, value in count.items():
        if value == 2:
            main_cards.append(key)
    result = len(main_cards) == 1
    if result:
        cards = main_cards * 2 + sorted([card[0] for card in hand if card[0] not in main_cards], reverse=True)
    else:
        cards = []
    return cards, result

def get_score(hand):
    cards, has_straight_flush = check_straight_flush(hand)
    if has_straight_flush:
        return [8, cards]
    cards, has_four_of_a_kind = check_four_of_a_kind(hand)
    if has_four_of_a_kind:
        return [7, cards]
    cards, has_full_house = check_full_house(hand)
    if has_full_house:
        return [6, cards]
    cards, has_flush = check_flush(hand)
    if has_flush:
        return [5, cards]
    cards, has_straight = check_straight(hand)
    if has_straight:
        return [4, cards]
    cards, has_three_of_a_kind = check_three_of_a_kind(hand)
    if has_three_of_a_kind:
        return [3, cards]
    cards, has_two_pair = check_two_pair(hand)
    if has_two_pair:
        return [2, cards]
    cards, has_one_pair = check_one_pair(hand)
    if has_one_pair:
        return [1, cards]
    cards = sorted([card[0] for card in hand], reverse=True)
    return [0, cards]

def create_hand(hand):
    result = []
    for card in hand:
        if card[0] == "T":
            value = 10
        elif card[0] == "J":
            value = 11
        elif card[0] == "Q":
            value = 12
        elif card[0] == "K":
            value = 13
        elif card[0] == "A":
            value = 14
        else:
            value = int(card[0])
        suit = card[1]
        result.append([value, suit])
    result.sort()
    return result

def solution():
    with open("0054_poker.txt") as f:
        hands = f.readlines()
        count = 0
        for hand in hands:
            hand1 = create_hand(hand[:15].split())
            hand2 = create_hand(hand[15:].split())
            score1 = get_score(hand1)
            score2 = get_score(hand2)
            if score1 > score2:
                count += 1
        return count

# Scoring system
# 0. High card
# 1. one pair
# 2. two pair
# 3. three of a kind
# 4. straight
# 5. flush
# 6. full house
# 7. four of a kind
# 8. straight flush

# if you have a straight, flush, straight flush, or nothing, then the high cards are in descending order.
# if you have 4 of a kind, 3 of a kind, or one pair, then the high cards are your combination, then all the leftovers in descending order.
# if you have a full house, then the high cards are your three of a kind cards and then your two of a kind cards.
# if you have 2 pair, then the first two cards are your best pair, the next two cards are your worse pair, and the last card is your leftover card

print(solution())