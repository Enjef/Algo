class Solution:
    def numberOfBeams(self, bank: List[str]) -> int: # 84.91% 11.41%
        prev = bank[0].count('1')
        res = 0
        for row in bank[1:]:
            cur = row.count('1')
            if not cur:
                continue
            res += prev * cur
            prev = cur
        return res

    def numberOfBeams_2nd_best_speed(self, bank: List[str]) -> int:
        ans = prev = 0
        for s in bank:
            c = s.count('1')
            if c:
                ans += prev * c
                prev = c
        return ans
