class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        out = ''
        current = ''
        i = 0
        while i < len(s):
            if s[i] not in current:
                current += s[i]
                if len(current) > len(out):
                    out = current
                i += 1
                continue
            index = current.index(s[i])
            current = current[index + 1:] + s[i]
            i += 1

        return len(out)