class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):  # 9.91% 71.21%
        n = len(difficulty)
        new = sorted(zip(difficulty, profit))
        max_profit = [-1] * n
        for i in range(n):
            difficulty[i] = new[i][0]
            profit[i] = new[i][1]
            if i == 0:
                max_profit[i] = new[i][1]
            else:
                max_profit[i] = max(max_profit[i-1], new[i][1])
        result = 0
        for candidate in worker:
            left, right = 0, n - 1
            ans = -1
            while left <= right:
                mid = (left+right)//2
                if difficulty[mid] > candidate:
                    right = mid - 1
                else:
                    ans = mid
                    left = mid + 1
            if ans == -1:
                continue
            result += max_profit[ans]
        return result
