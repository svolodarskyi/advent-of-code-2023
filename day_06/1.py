import math

with open("../inputs/day_06.txt", "r") as f:
    content = [l.strip() for l in f]

def calculate_ways(pair):
    ms, mm = map(int, pair)
    return sum(1 for i in range(1, ms + 1) if i * (ms - i) > mm)

ms = content[0].split(":")[1].strip().split()
mm = content[1].split(":")[1].strip().split()

races = list(zip(ms, mm)) 

num_of_ways = list(map(calculate_ways, races))

num_ways_prod = math.prod([ways for ways in num_of_ways])

print(num_ways_prod)
