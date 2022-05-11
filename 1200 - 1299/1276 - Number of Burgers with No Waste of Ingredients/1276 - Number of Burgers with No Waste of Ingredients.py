class Solution:
    def numOfBurgers(self, tomatoSlices, cheeseSlices):  # 75.18% 66.42%
        if (
                cheeseSlices * 2 > tomatoSlices or
                cheeseSlices * 4 < tomatoSlices or
                tomatoSlices % 2):
            return []
        jumbo = (tomatoSlices-2*cheeseSlices) // 2
        small = cheeseSlices - jumbo
        return [jumbo, small]

    def numOfBurgers_best_speed(
            self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices % 2 == 1:
            return []
        jumbo = tomatoSlices//2 - cheeseSlices
        if jumbo < 0:
            return []
        small = cheeseSlices - jumbo
        if small < 0:
            return []
        return [jumbo, small]

    def numOfBurgers_best_memory(
            self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        x = (tomatoSlices-2*cheeseSlices)/2
        y = (4*cheeseSlices-tomatoSlices)/2
        if int(x) == x and int(y) == y and x >= 0 and y >= 0:
            return [int(x), int(y)]
        return []
