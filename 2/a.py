with open("data.txt", "r+") as f:
    l = f.readlines()
    sum = 0
    for line in l:
        line = line.replace("\n", "")
        game, sets = line.split(": ")
        game_id = game.split(" ")[1]

        sets = sets.split("; ")
        enough = True
        for set in sets:
            allowance = {
                "red": 12,
                "green": 13,
                "blue": 14,
            }
            cubes = set.split(", ")
            if not enough:
                break
            for cube in cubes:
                _num, color = cube.split(" ")
                num = int(_num)
                v = allowance.get(color)
                if v is None:
                    enough = False
                    break
                if v - num < 0:
                    enough = False
                    break
                allowance[color] = v - num
        if enough:
            sum = sum + int(game_id)
        print(sets)
    print(sum)
