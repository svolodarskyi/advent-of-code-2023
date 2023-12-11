with open('../inputs/day_04.txt', 'r') as f:
    games = [l.strip().split(":")[1].strip() for l in f]

matches_count = []
cards_won = []

for game in games:
    left_deck, right_deck = game.split('|')
    left_deck = left_deck.split()
    right_deck = right_deck.split()
    common_elements = list(set(left_deck) & set(right_deck))
    matches_count.append(len(common_elements))
    

cards_won = [1] * len(matches_count)

for e, v in enumerate(matches_count):
    cards_won[e] += 1
    for i in range(e+1, v + 1 + e):
        cards_won[i] += cards_won[e]


print(sum(cards_won))


        