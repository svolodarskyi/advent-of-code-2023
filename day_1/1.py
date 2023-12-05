with open('./input/day_01.txt', 'r') as f:
    task_input = [l.strip() for l in f]

def first_digit(data: str, direction: str) -> str:
    if direction == 'f':
        data = data
    if direction == 'b':
        data = data[::-1]

    for _ in data:
        if _.isnumeric():
            return str(_)

sub_totals = [int(first_digit(i, 'f') + first_digit(i, 'b')) for i in task_input]
total = sum(sub_totals)

print(total)
