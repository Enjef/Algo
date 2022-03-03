class Solution:
    def dailyTemperatures(self, temperatures):  # 81.56% 68.88%
        n = len(temperatures)
        out = [0]*len(temperatures)
        stack = []
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                out[prev] = i-prev
            stack.append(i)
        return out
