class Solution:
    def reverseStr_join_reversed(self, s: str, k: int) -> str:
        if len(s) < k:
            s = s[::-1]
            return s
        if len(s) < 2*k:
            s = s[k-1::-1] + s[k:]
            return s
        for i in range(0, len(s), 2*k):
            s = s[:i] + ''.join(reversed(s[i:i+k])) + s[i+k:]
        return s

    def reverseStr(self, s: str, k: int) -> str:
        if len(s) < k:
            s = s[::-1]
            return s
        if len(s) < 2*k:
            s = s[k-1::-1] + s[k:]
            return s
        for i in range(0, len(s), 2*k):
            s = s[:i] + s[i:i+k][::-1] + s[i+k:]
        return s
