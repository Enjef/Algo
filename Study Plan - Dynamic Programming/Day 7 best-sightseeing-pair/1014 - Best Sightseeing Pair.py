class Solution:
    def maxScoreSightseeingPair(
            self,
            values: List[int]) -> int:  # 92.57% 57.59%
        i = 0
        prev = values[0]
        score = float('-inf')
        for j in range(1, len(values)):
            score = max(score, values[i] + values[j] - j + i)
            if values[j] + j >= prev:
                prev = values[j] + j
                i = j
        return score
