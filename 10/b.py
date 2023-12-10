from typing import Tuple, Dict, List

with open("data.txt", "r+") as f:
    l = f.readlines()
    sequences = list(map(lambda line: list(map(lambda s: int(s), line.split(" "))), l))

    def diff_sequence(sequence: list) -> list:
        return list(map(lambda i: sequence[i + 1] - sequence[i], range(len(sequence) - 1)))
    
    def get_first_of_sequence(sequence: List[int]) -> int:
        diff = diff_sequence(sequence)
        if len(diff) == 0 or all(map(lambda d: d == 0, diff)):
            return sequence[0]
        return sequence[0]- get_first_of_sequence(diff) 
     
    print(sum(list(map(lambda s: get_first_of_sequence(s), sequences))))