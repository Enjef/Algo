class Solution:  # 98.71% 40.89%
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = [0]
        out = [0]*n
        for i in range(1, n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                cur = stack.pop()
                out[cur] = i-cur
            stack.append(i)
        return out
