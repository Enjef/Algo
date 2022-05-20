class Solution:
    def minSwaps(self, s: str) -> int:  # 85.62% 24.30%
        total = 0
        stack = []
        for bracket in s:
            if bracket == ']':
                if stack:
                    stack.pop()
                else:
                    stack.append(bracket)
                    total += 1
            else:
                stack.append(bracket)
        return total

    def minSwaps_best_speed(self, s: str) -> int:
        count = 0
        for i in s:
            if i == '[':
                count += 1
            else:
                if count > 0:
                    count -= 1
        return (count + 1) // 2

    def minSwaps_best_memory(self, s: str) -> int:
        result = 0
        diff = 0
        for item in s:
            if item == ']':
                diff += 1
            else:
                diff -= 1
            result = max(result, diff)
        return (result + 1) // 2
