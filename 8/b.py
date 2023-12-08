from typing import Tuple, Dict
from math import gcd
from functools import reduce

with open("data.txt", "r+") as f:
    l = f.read()
    _instructions, _map_lines = l.split("\n\n")

    instructions = list(map(lambda s: 1 if s == "R" else 0, [*_instructions])) 
    map_lines = _map_lines.split("\n")
    m: Dict[str, Tuple[str, str]] = {}
    for line in map_lines:
        k, mi = line.split(" = ")    
        mi = mi.replace("(", "") 
        mi = mi.replace(")", "") 
        l, r = mi.split(", ")
        m[k] = (l, r)

    cur = list(filter(lambda k: k[2] == "A", m.keys()))
    i = 0
    found = [None] * len(cur)
    while True:
        for j in range(len(cur)):
            if cur[j][2] == "Z":
                found[j] = i
        if all(map(lambda f: f is not None, found)):
            break
        cur_instruction = instructions[i % len(instructions)]
        cur = list(map(lambda c: m[c][cur_instruction], cur))
        i += 1
    
    # s = 1
    # for f in found:
    #     s *= f
    lcm = reduce(lambda x,y:(x*y)//gcd(x,y), found)
    print(lcm)
