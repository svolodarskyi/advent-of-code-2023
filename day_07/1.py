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
        defines the type(ranking) being five_of_a_kind as 7 and high_card as 1.
        ranking in descending order.
    '''
    if sorted_count == [5]:
        #five_of_a_kind
        return 7
    elif sorted_count == [1,4]:
        #four_of_a_kind
        return 6
    elif sorted_count == [2,3]:
        #full_house
        return 5
    elif sorted_count == [1,1,3]:
        #three_kind
        return 4
    elif sorted_count == [1,2,2]:
        #two_pair
        return 3
    elif sorted_count == [1,1,1,2]:
        #one_pair
        return 2
    elif sorted_count == [1,1,1,1,1]:
        #high_card
        return 1
    

encoded_hands = {encode_hand(hand.split()[0]):hand.split()[1] for hand in hands}

hand_types = {}
#group hands by type
for encoded_hand in encoded_hands.keys():
    hand_counted = dict(Counter(encoded_hand))
    hand_counted_sorted = sorted(hand_counted.values())
    hand_types.setdefault(define_type(hand_counted_sorted), []).append(encoded_hand)

all_types = []
#when iterating keep the order assigned in the function `define_type`
for key in sorted(hand_types.keys(),reverse=False):
# #when sorting between items of the same type, sort them in acending order
     all_types += sorted(hand_types.get(key),reverse=False)

total_winnings = sum([int((o+1))*int(encoded_hands[i]) for o,i in enumerate(all_types)])    

print(total_winnings)