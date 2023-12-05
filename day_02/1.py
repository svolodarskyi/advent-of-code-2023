with open('./input/day_02.txt', 'r') as f:
    input_file = [l.strip() for l in f]

quialify_count = { 'red': 12, 'green': 13, 'blue': 14 }

def parse_game_id(game_stats: str) -> int:
    return int(game_stats.split(":")[0].split(" ")[1])

def get_color_count(game_stats: str) -> dict:
    game_color_count = {}
    game_sets = game_stats.split(":")[1]
    for game_set in game_sets.split(";"):
        for game_cubes in game_set.split(","):
            count, color = game_cubes.strip().split(' ')
            game_color_count[color] = max(game_color_count.get(color, 0), int(count))
    return game_color_count

def game_qualified(game_colors: dict) -> bool:
    qualify_status = 0
    for color, color_count in game_colors.items():
        if color_count <= quialify_count[color]:
            qualify_status +=1
    return qualify_status == 3


game_ids_qualified = sum([parse_game_id(game) for game in input_file if game_qualified(get_color_count(game))])

print(game_ids_qualified)