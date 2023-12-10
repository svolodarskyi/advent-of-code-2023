from functools import reduce
from operator import mul

with open('../inputs/day_04.txt', 'r') as f:
    games = [l.strip().split(":")[1].strip() for l in f]

result = []
for game in games:
    left_deck, right_deck = game.split('|')
    left_deck = left_deck.split()
    right_deck = right_deck.split()
    common_elements = list(set(left_deck) & set(right_deck))

    if len(common_elements):
        element_multipliers = [1 if i == 0 else 2 for i, _ in enumerate(common_elements)]
        multiplied = reduce(mul, element_multipliers, 1)
        result.append(element_multipliers)

result_sum = sum(result)
print(result)
        