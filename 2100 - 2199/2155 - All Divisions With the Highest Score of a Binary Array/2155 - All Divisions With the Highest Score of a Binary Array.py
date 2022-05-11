class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:  # 47.62% 67.06%
        n = len(nums)
        total = nums.count(1)
        max_score = total
        out = [0]
        left = 0
        right = total
        for i in range(n):
            left += nums[i] != 1
            right -= nums[i] == 1
            score = left + right
            if score == max_score:
                out.append(i+1)
            if score > max_score:
                max_score = score
                out = [i+1]
        return out

    def maxScoreIndices_best_speed(self, nums: List[int]) -> List[int]:
        nums = nums[::-1]
        maxScore = score = sum(nums)
        indices = [0]
        i = 1
        while nums:
            v = nums.pop()
            if v == 1:
                score -= 1
            else:
                score += 1
            if score > maxScore:
                indices = [i]
                maxScore = score
            elif score == maxScore:
                indices.append(i)
            i += 1
        return indices
