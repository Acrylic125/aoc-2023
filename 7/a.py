from typing import Tuple, Dict

with open("data.txt", "r+") as f:
    l = f.readlines()

    bids: Dict[str, int] = {}
    for line in l:
        name, bid = line.split(" ")
        bids[name] = int(bid)
    
    # A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2.
    card_types = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    card_type_scores: Dict[str, int] = {}
    for i in range(len(card_types)):
        card_type_scores[card_types[i]] = len(card_types) - i
    print(card_type_scores)
    
    def parse_hand(hand: str) -> Tuple[str, int]:
        cards = [*hand] 
        card_occurrences: Dict[str, int] = {}
        decoded = 0
        for card in cards:
            decoded = decoded * len(card_types) + card_type_scores[card]
            card_occurrences[card] = card_occurrences.get(card, 0) + 1
        # decoded = int(hand, 36)
        # Means all unique cards
        if len(card_occurrences) == 5:
            return "high_card", decoded
        # Means there is 1 pair
        elif len(card_occurrences) == 4:
            return "one_pair", decoded
        # 3 variants
        elif len(card_occurrences) == 3:
            counts = list(card_occurrences.values())
            counts.sort()
            if counts == [1, 2, 2]:
                return "two_pair", decoded
            elif counts == [1, 1, 3]:
                return "three_of_a_kind", decoded
            else:
                raise Exception(f"Invalid hand, {counts}")
        # Means five of a kind
        elif len(card_occurrences) == 2:
            counts = list(card_occurrences.values())
            counts.sort()
            if counts == [2, 3]:
                return "full_house", decoded
            return "four_of_a_kind", decoded
        # Means five of a kind
        elif len(card_occurrences) == 1:
            return "five_of_a_kind", decoded
        # Means there is 2 pairs
        
    kinds = ["high_card", "one_pair", "two_pair", "three_of_a_kind", "full_house", "four_of_a_kind", "five_of_a_kind"]

    hands = list(bids.keys()) 
    kind_scores: Dict[str, int] = {}
    
    for hand in hands:
        kind, score = parse_hand(hand)
        kind_scores[kind] = max(kind_scores.get(kind, 0), score)

    prev_kind_highest = 0
    for kind in kinds:
        c = prev_kind_highest + kind_scores.get(kind, 0)
        kind_scores[kind] = c
        prev_kind_highest = c
    
    hands = list(bids.keys())
    def get_hand_score(hand: str) -> int:
        kind, base_score = parse_hand(hand)
        return base_score + kind_scores[kind]
    
    hands.sort(key=get_hand_score)
    sum = 0
    for i in range(len(hands)):
        rank = i + 1
        hand_bid = bids[hands[i]]
        sum = sum + rank * hand_bid 
        print(f"{rank} {hands[i]} {hand_bid}")
    
    print(sum)