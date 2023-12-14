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

five_kind = []
four_kind = []
full_house = []
three_kind = []
two_pair = []
one_pair = []
high_card = []

for items in hands[:4]:
    hand, weight = items.split()
    print(encode_hand(hand))