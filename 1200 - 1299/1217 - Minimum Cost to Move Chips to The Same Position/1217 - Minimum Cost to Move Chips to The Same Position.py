class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:  # 66.99% 10.68%
        odd, even = [], []
        for pos in position:
            if pos % 2:
                odd.append(pos)
            else:
                even.append(pos)
        if len(odd) > len(even):
            return len(even)
        return len(odd)

    def minCostToMoveChips_best_speed(self, position: List[int]) -> int:
        o, e = 0, 0
        for i in range(len(position)):
            if position[i] % 2 == 1:
                o += 1
            else:
                e += 1
        return min(o, e)
