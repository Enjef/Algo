class Solution:
    def minPartitions(self, n: str) -> int:
        int_n = [int(x) for x in n]
        return max(int_n)

    def minPartitions_best(self, n: str) -> int:
        a = 9
        while a > 0:
            if str(a) in n:
                return a
            a -= 1
        return

    def minPartitions_fast_short(self, n: str) -> int:
        return int(max(n))
