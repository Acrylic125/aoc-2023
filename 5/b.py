import re
from typing import List

with open("data.txt", "r+") as f:
    l = f.readlines()
    cards = [1] * len(l)

    card_index = 0
    for line in l:

        line = line.replace("\n", "")
        card, nums = line.split(": ")
        winning, guess = nums.split(" | ")
        winning_nums = re.findall(r'\d+', winning)
        guess_nums = re.findall(r'\d+', guess)

        score = 0
        for num in guess_nums:
            if num in winning_nums:
                score = score + 1

        occ = cards[card_index]
        for i in range(1, score + 1):
            ni = card_index + i
            if ni >= len(cards):
                break
            cards[ni] = cards[ni] + occ

        card_index = card_index + 1
        
        # print(line)
        # print(winning_nums, guess_nums)
    print(cards)
    print(sum(cards))

