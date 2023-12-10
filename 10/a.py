from typing import Tuple, Dict, List, Union

with open("data.txt", "r+") as f:
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

    def print_dist_map():
        for line in dist_map:
            print(list(map(lambda c: f"{c}" if c is not None else ".", line)))
    
    current: List[Tuple[int, int]] = [start]
    dist_map: List[List[Union[None, int]]] = [[None for _ in range(width)] for _ in range(height)]
    dist_map[start[0]][start[1]] = 0
    
    checked = set() 
    checked.add(hash_pos(start))
    i = 0
    while len(current) > 0:
        next: List[Tuple[int, int]] = []
        # print("Iteration", i)
        # print_dist_map()
        i += 1
        for c in current:
            y, x = c
            char = m[y][x]
            dist = dist_map[y][x]
            
            dirs_for_current = indexed.get(char)
            if dirs_for_current is None:
                continue
            for d_index in dirs_for_current:
                dir = dirs[d_index]
                to_check = (y + dir[0], x + dir[1])
                if is_pos_out_of_bounds(to_check):
                    continue
                hashed = hash_pos(to_check)
                if hashed in checked:
                    continue
                
                to_check_char = m[to_check[0]][to_check[1]]
                to_check_dirs = indexed.get(to_check_char)
                if to_check_dirs is None:
                    continue

                can = False
                for to_check_dir_index in to_check_dirs:
                    to_check_dir = dirs[to_check_dir_index] 
                    n_to_check = (to_check[0] + to_check_dir[0], to_check[1] + to_check_dir[1])
                    if is_pos_out_of_bounds(n_to_check):
                        continue
                    if y == n_to_check[0] and x == n_to_check[1]:
                        can = True
                        break
                if not can:
                    continue

                checked.add(hashed)
                next.append(to_check)
                dist_map[to_check[0]][to_check[1]] = dist + 1
        current = next
    print(" ")
    print_dist_map()
    print(max([max(map(lambda c: c if c is not None else 0, line)) for line in dist_map]))
