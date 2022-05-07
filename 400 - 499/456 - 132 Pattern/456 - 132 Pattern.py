class Solution:
    def find132pattern(self, nums: List[int]) -> bool:  # 92.90% 33.50%
        third = float('-inf')
        stack = []
        for num in nums[::-1]:
            if num < third:
                return True
            while stack and stack[-1] < num:
                third = stack.pop()
            stack.append(num)
        return False
