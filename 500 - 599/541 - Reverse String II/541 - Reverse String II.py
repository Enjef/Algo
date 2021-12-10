class Solution:
    def reverseStr_join_reversed(self, s: str, k: int) -> str:  # 91.95% 73.50%
        if len(s) < k:
            s = s[::-1]
            return s
        if len(s) < 2*k:
            s = s[k-1::-1] + s[k:]
            return s
        for i in range(0, len(s), 2*k):
            s = s[:i] + ''.join(reversed(s[i:i+k])) + s[i+k:]
        return s

    def reverseStr(self, s: str, k: int) -> str:  # 78.70% 98.72%
        if len(s) < k:
            s = s[::-1]
            return s
        if len(s) < 2*k:
            s = s[k-1::-1] + s[k:]
            return s
        for i in range(0, len(s), 2*k):
            s = s[:i] + s[i:i+k][::-1] + s[i+k:]
        return s

    def reverseStr_mock(self, s: str, k: int) -> str:  # 78.70% 73.50%
        out = ''
        flag = True
        for i in range(0, len(s), k):
            if flag:
                out += s[i: i+k][::-1]
                flag = False
            else:
                out += s[i: i+k]
                flag = True
        if len(out) < len(s):
            out += s[i:i+len(s)-len(out)]
        return out
