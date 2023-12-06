with open("../inputs/day_03.txt", "r") as f:
    input_file = [l.strip() for l in f]

line_idx = list(range(len(input_file)))
char_idx = list(range(len(input_file[0])))
char_loc = {}
numb_loc = {}

char_prev = ''
numb = ''
numb_start_loc = None
numb_end_loc = None

#collect locations of the special characters
#collect starting and ending location of the numbers
for line_id in line_idx:
    for char_id in char_idx:
        char_curr = input_file[line_id][char_id]
        if not char_curr.isdigit() and char_prev.isdigit():
            numb_end_loc = char_id - 1
            numb_loc.setdefault(line_id, []).append(f"{numb}-{numb_start_loc}-{numb_end_loc}")
            numb = ""
        elif not char_curr.isdigit() and char_curr != '.':
            char_loc.setdefault(line_id, []).append(char_id)
        elif char_curr.isdigit() and numb == '':
            numb+=char_curr
            numb_start_loc = char_id
        elif char_curr.isdigit():
            numb+=char_curr
        char_prev = char_curr

