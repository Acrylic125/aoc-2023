import re
from typing import List, Tuple

with open("test.txt", "r+") as f:
    l = f.read()
    _maps = l.split("\n\n")
    seed = _maps[0]
    maps = _maps[1:]

    _values = list(map(lambda s: int(s), re.findall(r"\d+", seed)))
    value_pairings: List[Tuple[int, int]] = []
    for i in range(0, len(_values), 2):
        value_pairings.append([_values[i], _values[i + 1]])
    
    print(value_pairings)
    for m in maps:
        ms = m.split("\n")
        print(ms[0])
        map_rules = ms[1:]

        for rule in map_rules:
            dest_start, src_start, r = map(lambda s: int(s), rule.split(" "))
            new_pairings: List[Tuple[int, int]] = []

            for (low_v, vr) in value_pairings:
                low_bounds, high_bounds = src_start, src_start + r - 1
                high_v = low_v + vr - 1

                if high_v > high_bounds:
                    right_low = max(low_v, high_bounds)
                    right_high = high_bounds
                    right_pairing = (right_low, right_high - right_low)
                    if right_pairing[1] > 0:
                        new_pairings.append(right_pairing)
                if low_v < low_bounds:
                    left_low = low_v
                    left_high = min(low_v, low_bounds)
                    left_pairing = (left_low, left_high - left_low)
                    if left_pairing[1] > 0:
                        new_pairings.append(left_pairing)
                
                # Check if v is in bounds
                if low_v >= low_bounds and high_v <= high_bounds:
                    new_pairings.append((low_v - src_start + dest_start, vr))
                
                # Handle intersection
                # if low_v <= low_bounds and high_v <= high_bounds:
                #     low_intersect = low_bounds
                #     high_intersect = high_v
                    
                #     intersect_pairing = (low_intersect - src_start + dest_start, high_intersect - low_intersect + 1)
                #     new_pairings.append(intersect_pairing)
                # elif low_v >= low_bounds and high_v >= high_bounds:
                #     low_intersect = low_v
                #     high_intersect = high_v
                    
                #     intersect_pairing = (low_intersect - src_start + dest_start, high_intersect - low_intersect + 1)
                #     new_pairings.append(intersect_pairing)
                # else:
                #     pairing = (low_v, vr)
                #     new_pairings.append(pairing)
            print([dest_start, src_start, r], value_pairings, new_pairings)
            value_pairings = new_pairings
    
    print(min(list(map(lambda p: p[0], value_pairings))))
    # print(maps)

