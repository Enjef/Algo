class Solution:
    def wateringPlants(
            self, plants: List[int], capacity: int) -> int:  # 42.25% 99.31%
        cur = capacity
        out = 0
        for i in range(len(plants)):
            if cur < plants[i]:
                out += i * 2 + 1
                cur = capacity - plants[i]
            else:
                out += 1
                cur -= plants[i]
        return out
