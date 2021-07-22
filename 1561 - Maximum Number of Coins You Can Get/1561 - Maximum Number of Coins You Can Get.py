class Solution:
    def maxCoins(self, piles: List[int]) -> int:  # 89.55% 24.06%
        out = 0
        piles.sort()
        triples = len(piles) // 3
        for i in range(len(piles)-2, triples-1, -2):
            out += piles[i]
        return out

    def maxCoins_best(self, piles: List[int]) -> int:
        coin_piles = sorted(piles, reverse=True)
        coins = 0
        for i in range(1, int(len(piles)/3*2), 2):
            coins += coin_piles[i]
        return coins

    def maxCoins_short_top_3(self, piles: List[int]) -> int:
        return sum(sorted(piles)[len(piles)//3 :: 2])
