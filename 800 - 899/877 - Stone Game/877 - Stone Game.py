class Solution:
    def stoneGame(self, piles: List[int]) -> bool: # 97.57% 96.56%
        alice = 0
        bob = 0
        piles.sort()
        first = True
        while piles:
            if first:
                first = False
                alice += piles.pop()
            else:
                first = True
                bob += piles.pop()
        return alice > bob

    def stoneGame_best_speed(self, piles: List[int]) -> bool:
        return True
