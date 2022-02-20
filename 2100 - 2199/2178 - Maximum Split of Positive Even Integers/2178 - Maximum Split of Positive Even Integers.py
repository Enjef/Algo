class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]: #new 50.00% 100.00%
        if finalSum%2:
            return []
        cur = 2
        out = []
        cur_sum = 0
        while cur_sum + cur <= finalSum:
            cur_sum += cur
            out.append(cur)
            cur += 2
        out[-1] += finalSum-cur_sum
        return out

    def maximumEvenSplit_best_speed_and_mem(self, finalSum: int) -> List[int]:
        if finalSum % 2 == 1:
            return []
        finalSum //= 2
        i = 1
        ans = []
        while finalSum > 2*i:
            finalSum -= i
            ans.append(2*i)
            i += 1
        if finalSum > 0:
            ans.append(2*finalSum)
        return ans
