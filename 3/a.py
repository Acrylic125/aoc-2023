from typing import List

with open("data.txt", "r+") as f:
    l = f.readlines()
    sum = 0
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
    def check_has_adj(x: int, y: int) -> bool:
        for dir in dirs:
            dx, dy = dir
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= width or ny < 0 or ny >= height:
                continue
            char = m[ny][nx]
            if not char.isdigit() and char != ".":
                return True 
        return False 
    
    sum = 0
    for y, line in enumerate(l):
        num_str = ""
        num_has_adj = False
        for x, c in enumerate(line):
            if c.isdigit():
                num_str = num_str + c
                if not num_has_adj:
                    num_has_adj = check_has_adj(x, y)
            else:
                if num_str != "":
                    if num_has_adj:
                        sum = sum + int(num_str)
                    num_str = ""
                    num_has_adj = False  
    print(sum)
