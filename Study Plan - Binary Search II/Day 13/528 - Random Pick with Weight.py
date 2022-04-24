class Solution:  # 33.96% 80.05%
    def __init__(self, w: List[int]):
        self.arr = []
        self.total = 0
        for el in w:
            self.total += el
            self.arr.append(self.total)

    def pickIndex(self) -> int:
        target = random.randint(0, self.total-1)
        left, right = 0, len(self.arr)
        while left < right:
            mid = (left+right)//2
            if self.arr[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left
