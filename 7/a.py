from typing import Tuple, Dict

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

    cur = "AAA"
    end = "ZZZ"
    i = 0
    while True:
        if cur == end:
            break
        cur_instruction = instructions[i % len(instructions)]
        cur = m[cur][cur_instruction]  
        i += 1
    
    print(i)
