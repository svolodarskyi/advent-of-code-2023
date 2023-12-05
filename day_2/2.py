from functools import reduce
with open('./input.txt', 'r') as f:
    input_file = [l.strip() for l in f]

quialify_count = { 'red': 12, 'green': 13, 'blue': 14 }

def get_color_count(game_stats: str) -> dict:
    game_color_count = {}
    game_sets = game_stats.split(":")[1]
    for game_set in game_sets.split(";"):
        for game_cubes in game_set.split(","):
            count, color = game_cubes.strip().split(' ')
            game_color_count[color] = max(game_color_count.get(color, 0), int(count))
    return game_color_count

def multiply_count(color_count: dict) -> int:
    return reduce(lambda x,y: x*y, color_count.values(), 1)

color_count_sum_product = sum([multiply_count(get_color_count(game)) for game in input_file])

print(color_count_sum_product)

