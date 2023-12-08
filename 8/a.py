import re
from typing import List

with open("data.txt", "r+") as f:
    l = f.read()
    _maps = l.split("\n\n")
    seed = _maps[0]
    maps = _maps[1:]

    values = list(map(lambda s: int(s), re.findall(r"\d+", seed)))
    for m in maps:
        ms = m.split("\n")
        print(ms[0])
        map_rules = ms[1:]

        mapped_indices = []
        for rule in map_rules:
            dest_start, src_start, r = map(lambda s: int(s), rule.split(" "))
            new_values = []

            i = 0
            for v in values:
                if i not in mapped_indices and (v >= src_start and v < src_start + r):
                    new_values.append(v - src_start + dest_start)
                    mapped_indices.append(i)
                else:
                    new_values.append(v)
                i = i + 1
            print([dest_start, src_start, r], values, new_values)
            values = new_values
    
    print(values)
    print(min(values))
    # print(maps)
