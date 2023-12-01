import re

mappings = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

with open("data.txt", "r+") as f:
    l = f.readlines()
    sum = 0
    for line in l:
        line = line.replace("\n", "")
        print(line)
        char_count = len(line)
        first, second = None, None
        for i in range(0, char_count):
            s = line[i]
            if s.isdigit():
                if first is None:
                    first = s
                else:
                    second = s
            else:
                for word, digit in mappings.items():
                    failed = False
                    for j in range(0, len(word)):
                        ij = i + j
                        if ij >= char_count:
                            failed = True
                            break
                        if line[ij] != word[j]:
                            failed = True
                            break
                    if failed:
                        continue
                    if first is None:
                        first = digit
                    else:
                        second = digit
                    break
                    
        if second is None:
            second = first
        joined = int(f"{first}{second}")
        sum = sum + joined
        print(f"{first} {second} {joined}")
    print(sum)
