import re
from typing import List

with open("data.txt", "r+") as f:
    l = f.readlines()
    sum = 0
    for line in l:
        line = line.replace("\n", "")
        card, nums = line.split(": ")
        winning, guess = nums.split(" | ")
        winning_nums = re.findall(r'\d+', winning)
        guess_nums = re.findall(r'\d+', guess)

        score = 0
        for num in guess_nums:
            if num in winning_nums:
                if score == 0:
                    score = 1
                else:
                    score = score * 2
        sum = sum + score
        
        # print(line)
        # print(winning_nums, guess_nums)
    print(sum)
