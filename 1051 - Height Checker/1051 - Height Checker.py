class Solution:
    def heightChecker(self, heights: List[int]) -> int:  # 96.32% 72.36%
        expected = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if expected[i] != heights[i]:
                count += 1
        return count
