from collections import Counter

with open('../inputs/day_07.txt', 'r') as f:
    hands = [l.strip() for l in f]

def encode_ch(ch: str) -> str:
    encoding = {  
        "2": "A",
        "3": "B",
        "4": "C",
        "5": "D",
        "6": "E",
        "7": "F",
        "8": "G",
        "9": "H",
        "T": "I",
        "J": "J",
        "Q": "K",
        "K": "L",
        "A": "M"
    }
    return encoding.get(ch)

def encode_hand(hand: str)-> str:
    return "".join([encode_ch(ch) for ch in hand])


def define_type(sorted_count: list[int]) -> int:
    ''' 
        defines the type(ranking) being five_of_a_kind as 1 and high_card as 8.
        ranking in ascending order, being 1 is "highter" than 8.
        five_of_a_kind > four_of_a_kind > full_house > three_kind > two_pair > one_pair > high_card
    '''
    if sorted_count == [5]:
        return 1
    elif sorted_count == [1,4]:
        return 2
    elif sorted_count == [2,3]:
        return 3
    elif sorted_count == [1,1,3]:
        return 4
    elif sorted_count == [1,2,2]:
        return 5
    elif sorted_count == [1,1,1,2]:
        return 6
    elif sorted_count == [1,1,1,1,1]:
        return 7
    

hand_types = {}
encoded_hands = {encode_hand(hand.split()[0]):hand.split()[1] for hand in hands}

for encoded_hand in encoded_hands.keys():
    hand_counted = dict(Counter(encoded_hand))
    hand_counted_sorted = sorted(hand_counted.values())
    hand_types.setdefault(define_type(hand_counted_sorted), []).append(encoded_hand)

print(sorted(hand_types[2]))