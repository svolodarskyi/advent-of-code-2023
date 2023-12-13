import math

with open("../inputs/day_06.txt", "r") as f:
    ms, mm = map(int,(l.strip().split(":")[1].strip().replace(" ", "") for l in f))

num_of_ways = sum(1 for i in range(1, ms + 1) if i * (ms - i) > mm)

print(num_of_ways)
