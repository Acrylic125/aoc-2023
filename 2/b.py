with open("data.txt", "r+") as f:
    l = f.readlines()
    sum = 0
    for line in l:
        line = line.replace("\n", "")
        game, sets = line.split(": ")
        game_id = game.split(" ")[1]

        sets = sets.split("; ")
        req = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        for set in sets:
            cubes = set.split(", ")
            for cube in cubes:
                _num, color = cube.split(" ")
                num = int(_num)
                v = req.get(color)
                if v is None:
                    continue
                req[color] = max(v, num)
        power = req["red"] * req["green"] * req["blue"]
        sum = sum + power
        print(sets)
    print(sum)
