from collections import Counter

with open('../inputs/day_07.txt', 'r') as f:
    hands = [l.strip() for l in f]

def encode_ch(ch: str) -> str:
    encoding = {  
        "J": "A",
        "2": "B",
        "3": "C",
        "4": "D",
        "5": "E",
        "6": "F",
        "7": "G",
        "8": "H",
        "9": "I",
        "T": "J",
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

def swap_joker_and_recount(hand_counted: dict, encrypted_joker: str) -> list:
    hand_counted_list = list(hand_counted.values())
    if len(hand_counted_list)>1:
        jocker_count = hand_counted.get(encrypted_joker)
        hand_counted_list.remove(jocker_count)
        #swap Jocker card for the one which has max value in a hand
        max_value = max(hand_counted_list)
        max_index = hand_counted_list.index(max_value)
        hand_counted_list[max_index] += jocker_count
    return hand_counted_list

encoded_hands = {encode_hand(hand.split()[0]):hand.split()[1] for hand in hands}
#'A' is encrypted joker 'J' 
encrypted_joker = 'A'
hand_types = {}

for encoded_hand in encoded_hands.keys():
    hand_counted = dict(Counter(encoded_hand))
    if encrypted_joker in hand_counted:
        hand_counted_sorted = sorted(swap_joker_and_recount(hand_counted), encrypted_joker)
    else:
        hand_counted_sorted = sorted(hand_counted.values())
    hand_types.setdefault(define_type(hand_counted_sorted), []).append(encoded_hand)

all_types = []
#when iterating keep the order assigned in the function `define_type`
for key in sorted(hand_types.keys(),reverse=False):
#when sorting between items of the same type, sort them in acending order M > A
     all_types += sorted(hand_types.get(key),reverse=False)

total_winnings = sum([int((o+1))*int(encoded_hands[i]) for o,i in enumerate(all_types)])    

print(total_winnings)