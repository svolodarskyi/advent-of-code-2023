with open('./input/day_01.txt', 'r') as f:
    input_file = [l.strip() for l in f]

valid_digits = {
    "one" : 1,
    "two" : 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def first_digit(data: str, direction: str) -> str:
    if direction == 'f':
        character_indices = list(range(len(data)))
    if direction == 'b':
        character_indices = list(range(len(data)))[::-1]
    
    for char_posit in character_indices:
        if data[char_posit].isdigit():
            return str(data[char_posit])
        for digit_name in list(valid_digits.keys()):
            if data[char_posit:].startswith(digit_name):
                return str(valid_digits.get(digit_name))

sum_of_digits = sum([int(first_digit(item, 'f') + first_digit(item, 'b')) for item in input_file])

print(sum_of_digits)


        


