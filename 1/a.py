with open("test.txt", "r+") as f:
    l = f.readlines()
    sum = 0
    for line in l:
        line = line.replace("\n", "")
        char_count = len(line)
        first, second = None, None
        for i in range(0, char_count):
            s = line[i]
            if s.isdigit():
                if first is None:
                    first = s
                else:
                    second = s
        if second is None:
            second = first
        joined = int(f"{first}{second}")
        sum = sum + joined
        print(f"{first} {second} {joined}")
    print(sum)
