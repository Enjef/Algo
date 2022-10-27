class Solution:
    # 48.46% 68.16% (98.18% 14.94%)
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        ranks = Counter(ranks)
        suits = set(suits)
        print(ranks)
        if len(suits) == 1:
            return 'Flush'
        elif 3 <= max(ranks.values()):
            return 'Three of a Kind'
        elif 2 <= max(ranks.values()):
            return 'Pair'
        return 'High Card'


class Solution_best_speed:
    def bestHand_1st(self, ranks: List[int], suits: List[str]) -> str:
        d1 = Counter(suits)
        d2 = Counter(ranks)
        n_suits = 0
        for k, v in d1.items():
            if v > n_suits:
                n_suits = v

        n_ranks = 0
        for k, v in d2.items():
            if v > n_ranks:
                n_ranks = v

        if n_suits == 5:
            return 'Flush'
        if n_ranks >= 3:
            return 'Three of a Kind'
        if n_ranks >= 2:
            return 'Pair'
        return 'High Card'

    def bestHand_2nd(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return "Flush"
        set_ranks = sorted([ranks.count(i) for i in set(ranks)])
        if set_ranks[-1] >= 3:
            return "Three of a Kind"
        elif set_ranks[-1] == 2:
            return "Pair"
        else:
            return "High Card"


class Solution_best_memory:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return "Flush"
        m = max(Counter(ranks).values())
        if m >= 3:
            return "Three of a Kind"
        if m == 2:
            return "Pair"
        return "High Card"
