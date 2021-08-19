class Solution:
    def longestNiceSubstring(self, s: str) -> str:  # 5.86% 66.16%
        if len(s) < 3:
            return s if self.is_nice(s) else ''
        for size in range(len(s), -1, -1):
            for i in range(len(s)-size+1):
                if self.is_nice(s[i:i+size]):
                    return s[i:i+size]
        return ''

    def is_nice(self, arr):
        for char in arr:
            if char.isupper():
                if char.lower() in arr:
                    arr = arr.replace(char.lower(), '').replace(char, '')
            else:
                if char.upper() in arr:
                    arr = arr.replace(char.upper(), '').replace(char, '')
        if not arr:
            return True
        return False

    def is_nice_swapcase(self, arr):  # 44.25% 39.05%
        for char in arr:
            if char.swapcase() not in arr:
                return False
        return True

    def longestNiceSubstring_all_subs(self, s: str) -> str:  # 42.08% 66.16%
        out = ''
        for i in range(len(s)):
            for j in range(len(s), i, -1):
                if self.is_nice_swapcase(s[i:j+1]):
                    out = max(out, s[i:j+1], key=len)
        return out

    def longestNiceSubstring_best_speed(self, s: str) -> str:
        if len(s) < 2:
            return ""
        se = set()
        for i in s:
            se.add(i)
        for i in range(0, len(s)):
            if (
                s.find(str(s[i]).lower()) != -1 and
                s.find(str(s[i]).upper()) != -1
            ):
                continue
            prev = self.longestNiceSubstring(s[:i])
            nextt = self.longestNiceSubstring(s[i+1:])
            return prev if len(prev) >= len(nextt) else nextt
        return s

    def longestNiceSubstring_top_five_speed(self, s: str) -> str:
        if len(s) < 2:
            return ''
        for i in range(len(s)):
            if s[i].swapcase() not in s:
                front = self.longestNiceSubstring(s[:i])
                tail = self.longestNiceSubstring(s[i+1:])
                return max(front, tail, key=len)
        return s
