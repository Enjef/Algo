class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:  # 91.85% 29.81%
        coord = len(s)
        arr = [coord]*coord
        for i in range(len(s)):
            if s[i] == c:
                coord = 0
            arr[i] = coord
            coord += 1
        for i in range(len(s)-1, -1, -1):
            if s[i] == c:
                coord = 0
            arr[i] = min(arr[i], coord)
            coord += 1
        return arr

    def shortestToChar_best(self, s: str, c: str) -> List[int]:
        ans = []
        prev = float('-inf')
        for i, x in enumerate(s):
            if x == c:
                prev = i
            ans.append(i - prev)
        prev = float('inf')
        for i in range(len(s) - 1, -1, -1):
            if s[i] == c:
                prev = i
            ans[i] = min(ans[i], prev - i)
        return ans

    def shortestToChar_best_memory(self, s: str, c: str) -> List[int]:
        dic = [idx for idx, ch in enumerate(s) if ch == c]
        n, m = len(s), len(dic)
        if len(dic) == 1:
            return [abs(idx - dic[0]) for idx in range(n)]
        lo, hi = 0, 1
        res = []
        for i in range(n):
            if i > dic[hi]:
                lo = hi
                if hi < m - 1:
                    hi += 1
            res.append(min(abs(i - dic[lo]), abs(i - dic[hi])))
        return res
