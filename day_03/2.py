with open("../inputs/day_03.txt", "r") as f:
    input_file = [l.strip() for l in f]

line_idx = list(range(len(input_file)))
char_idx = list(range(len(input_file[0])))
char_loc = {}
numb_loc = {}
numb_around = {}
char_prev = ""
numb = ''
numb_start_loc = None
numb_end_loc = None

numb_around_char = []

#collect locations of the special characters
#collect starting and ending location of the numbers
for line_id in line_idx:
    for char_id in char_idx:
        char_curr = input_file[line_id][char_id]
        if not char_curr.isdigit() and char_prev.isdigit():
            numb_end_loc = char_id - 1
            numb_loc.setdefault(line_id, []).append(f"{numb}-{numb_start_loc}-{numb_end_loc}")
            numb = ""
            char_prev = ""
            numb_end_loc = None
            numb_start_loc = None
            if char_curr == '*':
                char_loc.setdefault(line_id, []).append(char_id)
        elif not char_curr.isdigit() and char_curr == '*':
            char_loc.setdefault(line_id, []).append(char_id)
            char_prev = char_curr
        elif char_curr.isdigit() and numb == '':
            numb+=char_curr
            numb_start_loc = char_id
            char_prev = char_curr
        elif char_curr.isdigit():
            numb+=char_curr
            if char_id == max(char_idx):
                numb_end_loc = char_id
                numb_loc.setdefault(line_id, []).append(f"{numb}-{numb_start_loc}-{numb_end_loc}")
                numb = ""
                char_prev = ""
                numb_end_loc = None
                numb_start_loc = None
        

for line_num, char_locat in char_loc.items():
    num_around = numb_loc.get(line_num-1, [])  + numb_loc.get(line_num, [])  + numb_loc.get(line_num+1, []) 
    for ch in char_locat: 
        for number in num_around:
            _num, _start_loc, _end_loc = tuple(number.split('-'))
            if int(ch) >= (int(_start_loc) - 1) and int(ch) <= (int(_end_loc) + 1):
                numb_around.setdefault(str(line_num)+"-"+str(ch), []).append(_num)


result = sum([int(v[0]) * int(v[1]) for k, v in numb_around.items() if len(v) == 2])

print(result)