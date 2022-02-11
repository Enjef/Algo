class Solution:
    def diStringMatch(self, s: str) -> List[int]:  # 9.78% 94.36%
        n = len(s)
        i, j, idx = 0, n, 0
        out = []
        while i <= j:
            if s[idx] == 'I':
                out.append(i)
                i += 1
            else:
                out.append(j)
                j -= 1
            if idx < n-1:
                idx += 1
        return out

    def diStringMatch_best_speed(self, s: str) -> List[int]:
        i, j, ans = 0, len(s), []
        for x in s:
            if x == 'I':
                ans.append(i)
                i += 1
            else:
                ans.append(j)
                j -= 1
        ans.append(j)
        return ans
