from typing import List, Dict

with open("data.txt", "r+") as f:
    l = f.readlines()
    m: List[List[str]] = []
    width, height = len(l[0].replace("\n", "")), len(l)
    print(width, height)

    for line in l:
        layer = []
        for c in line:
            layer.append(c)
        m.append(layer)

    dirs = [
        [-1, -1],
        [-1, 0],
        [-1, 1],
        [0, -1],
        [0, 1],
        [1, 1],
        [1, 0],
        [1, -1],
    ]
    def get_adj_gear(x: int, y: int) -> List[int]:
        gears: List[int] = []
        for dir in dirs:
            dx, dy = dir
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= width or ny < 0 or ny >= height:
                continue
            char = m[ny][nx]
            if char == "*":
                gear = nx + ny * width
                gears.append(gear)
        return gears
    
    gears: Dict[int, List[int]] = {}
    for y, line in enumerate(l):
        num_str = ""
        considered = set()
        for x, c in enumerate(line):
            if c.isdigit():
                num_str = num_str + c
                adj_gears = get_adj_gear(x, y)
                for gear in adj_gears:
                    if gear in considered:
                        continue
                    considered.add(gear)
            else:
                if num_str != "":
                    for gear in considered:
                        if gear not in gears:
                            gears[gear] = []
                        gears[gear].append(int(num_str))
                    num_str = ""
                    considered = set()
    
    sum = 0
    for gear_values in gears.values():
        if len(gear_values) == 2:
            sum = sum + gear_values[0] * gear_values[1]
    print(sum)

