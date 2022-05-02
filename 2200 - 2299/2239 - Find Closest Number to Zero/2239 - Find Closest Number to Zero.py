class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:  # 7.51% 88.48%
        result = float('-inf')
        min_dist = float('inf')
        for num in nums:
            if abs(num) == min_dist:
                result = max(result, num)
            elif abs(num) < min_dist:
                min_dist = abs(num)
                result = num
        return result

    def findClosestNumber_best_speed(self, nums: List[int]) -> int:
        res = [abs(i) for i in nums]
        return min(res) if min(res) in nums else -min(res)

    def findClosestNumber_best_memory(self, nums: List[int]) -> int:
        ans = None
        mini = float('inf')
        for i in nums:
            curr = abs(i)
            if curr < mini or (curr == mini and (ans is None or i > ans)):
                ans = i
                mini = curr
        return ans
