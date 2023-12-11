with open("../inputs/day_05.txt", "r") as input_text:
    content = input_text.read()

blocks = content.split('\n\n')

seeds = blocks[0]
mapping = blocks[1:]
seeds = seeds.split(":")[1].split()


class Parser():

    def __init__(self, seed, mapping):
        self.dest_target = seed
        self.mapping = mapping
    
    def parse_map(self, _map: str) -> None:
        mapping_sets = _map.split(':\n')[1].split('\n')
        for item in mapping_sets:
            dest, source, range_len = item.split()
            if int(source)+int(range_len) >= int(self.dest_target) >= int(source):
                new_dest_target = int(dest) + int(self.dest_target) - int(source)
                self.dest_target = new_dest_target
                break
        # comment for parse_map:
        # Any source numbers that aren't mapped correspond to the same destination number
                 
    def process(self):
        for _map in self.mapping:
            self.parse_map(_map.strip())
        return self.dest_target


location_min = min([Parser(seed, mapping).process() for seed in seeds])

print(location_min)


