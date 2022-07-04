class Solution:
    # 53.26% 73.73%
    def backspaceCompare(self, s: str, t: str) -> bool:
        def helper(word):
            out = []
            for char in word:
                if char == '#':
                    if out:
                        out.pop()
                else:
                    out.append(char)
            return out
        return helper(s) == helper(t)
