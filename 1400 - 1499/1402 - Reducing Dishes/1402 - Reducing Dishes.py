class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int: # 93.72% 93.50%
        satisfaction.sort(reverse=True)
        total = 0
        prev = 0        
        running = 0
        if satisfaction[0] < 0:
            return total
        for num in satisfaction:
            total += num + running
            running += num
            if total <= prev:
                return prev
            prev = total
        return total

    def maxSatisfaction_best_speed(self, satisfaction: List[int]) -> int:
        ma = 0
        s = satisfaction
        n = len(s)
        s.sort(reverse=True)
        p = 0
        pre = 0
        for i in range(n):
            tmp = p + pre + s[i]
            ma = max(ma, tmp)
            p = tmp
            pre = pre + s[i]
        return ma

    def maxSatisfaction_best_memory(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse = True)
        summ = satisfaction[0]
        for i in range(1, len(satisfaction)):
            curr = satisfaction[i]
            satisfaction[i] += satisfaction[i-1] + summ
            summ += curr
        return 0 if max(satisfaction) < 0 else max(satisfaction) 
