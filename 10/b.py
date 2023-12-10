from typing import Tuple, Dict, List, Union

with open("test4.txt", "r+") as f:
    l = f.readlines()

    m = list(map(lambda line: list(line.strip()), l))
    width = len(m[0])
    height = len(m)
    
    start: Tuple[int, int] = None
    for i in range(height):
        for j in range(width):
            if m[i][j] == "S":
                start = (i, j)
                break

    print(width, height)
    print(start) 
    
    # F-7  ---> (+0, +1)
    # | |   |
    # L-J  \/   (+1, +0)
    dirs = [
        (1, 0), # | F 7 
        (0, 1), # - F L 
        [-1, 0], # | L J
        (0, -1), # - 7 J
    ]
    indexed = {
        "S": [0, 1, 2, 3],
        "O": [0, 1, 2, 3],
        "-": [1, 3],
        "|": [0, 2],
        "F": [0, 1],
        "7": [0, 3],
        "J": [2, 3],
        "L": [1, 2],
    }

    def is_pos_out_of_bounds(pos: Tuple[int, int]) -> bool:
        return pos[0] < 0 or pos[0] >= height or pos[1] < 0 or pos[1] >= width
    
    def hash_pos(pos: Tuple[int, int]) -> int:
        return pos[0] + pos[1] * width

    def print_map():
        for line in m:
            print(list(map(lambda c: f"{c}" if c is not None else ".", line)))
    
    current: List[Tuple[int, int]] = [start]
    while True:
        free_pos: Tuple[int, int] = None
        for y in range(height):
            for x in range(width):
                if m[y][x] == ".":
                    free_pos = (y, x)
                    break
            if free_pos is not None:
                break
        if free_pos is None:
            break
        print_map()

        is_region_inner = True 
        inner_region_sizes: List[int] = []
        current: List[Tuple[int, int]] = [free_pos]
        m[free_pos[0]][free_pos[1]] = "O"
        tiles = 0
        while len(current) > 0:
            next: List[Tuple[int, int]] = []
            for n in current:
                y, x = n
                char = m[y][x]
                char_dirs_indices = indexed.get(char) 
                
                for dir_index in char_dirs_indices:
                    dir = dirs[dir_index]
                    dy, dx = dir
                    ny, nx = y + dy, x + dx
                    if is_pos_out_of_bounds((ny, nx)):
                        is_region_inner = False
                        continue
                    if m[ny][nx] == ".":
                        m[ny][nx] = "O"
                        next.append((ny, nx))
                        tiles += 1
            current = next
        