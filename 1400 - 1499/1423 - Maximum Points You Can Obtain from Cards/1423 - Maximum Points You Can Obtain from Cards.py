class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:  # 32.61% 40.17%
        n = len(cardPoints)
        total = sum(cardPoints)
        if k == n:
            return total
        cur = sum(cardPoints[-k:])
        out = cur
        for i in range(k):
            cur += cardPoints[i] - cardPoints[-k+i]
            out = max(out, cur)
        return out

    def maxScore_v2(self, cardPoints: List[int], k: int) -> int:  # 90.51% 17.27%
        n = len(cardPoints)
        if k == n:
            return sum(cardPoints)
        out = cur = sum(cardPoints[-k:])
        for i in range(k):
            cur += cardPoints[i] - cardPoints[-k+i]
            out = max(out, cur)
        return out

    def maxScore_best_speed(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        totalPoints = sum(cardPoints)
        r = n - k
        if r == 0:
            return totalPoints
        Min = float('inf')
        lo, hi = 0, r
        Sum = sum(cardPoints[lo:hi])
        Min = Sum
        for i in range(0, n-r):
            valPop = cardPoints[lo]
            valAdd = cardPoints[hi]
            Sum += valAdd - valPop
            if Sum < Min:
                Min = Sum
            lo += 1
            hi += 1
        return totalPoints - Min

    def maxScore_2nd_best_speed(self, cardPoints: List[int], k: int) -> int:        
        return sum(cardPoints[:k]) + max(chain([0], accumulate(cardPoints[-i] - cardPoints[k-i] for i in range(1, k+1))))

    def maxScore_best_memory(self, cardPoints: List[int], k: int) -> int:
        window_sum = sum(cardPoints[0:k])
        answer = window_sum
        for idx in range(k):
            window_sum += cardPoints[-1 - idx]
            window_sum -= cardPoints[k - 1 - idx]
            answer = max(answer, window_sum)
        return answer
