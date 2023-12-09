from typing import Tuple, Dict, List

with open("data.txt", "r+") as f:
    l = f.readlines()
    sequences = list(map(lambda line: list(map(lambda s: int(s), line.split(" "))), l))

    def diff_sequence(sequence: list) -> list:
        return list(map(lambda i: sequence[i + 1] - sequence[i], range(len(sequence) - 1)))
    
    def get_last_of_sequence(sequence: List[int]) -> int:
        diff = diff_sequence(sequence)
        if len(diff) == 0 or all(map(lambda d: d == 0, diff)):
            return sequence[len(sequence) - 1]
        return get_last_of_sequence(diff) + sequence[len(sequence) - 1]
     
    print(sum(list(map(lambda s: get_last_of_sequence(s), sequences))))
