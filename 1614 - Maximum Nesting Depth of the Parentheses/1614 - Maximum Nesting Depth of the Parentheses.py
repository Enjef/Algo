class Solution:
    def maxDepth(self, s: str) -> int:  # 86.10% 38.63%
        out = 0
        count = 0
        for char in s:
            if char == '(':
                count += 1
            if char == ')':
                count -= 1
            out = max(out, count)
        return out

    def maxDepth_best(self, s: str) -> int:
        p = []
        nd = 0
        for c in s:
            if(c == '('):
                p.append('(')
                if(len(p) > nd):
                    nd = len(p)
            elif(c == ')'):
                if(len(p)):
                    p.pop()
        return nd
