class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count, i, j = 0, len(g) - 1, len(s) - 1
        while i >= 0 and j >= 0:
            if s[j] >= g[i]:
                count += 1
                i -= 1
                j -= 1
            else:
                i -= 1
        return count
