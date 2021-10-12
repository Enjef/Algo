class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:  # 44.06% 53.55%
        if len(s) == 1:
            return 1
        max_s = ''
        cur = ''
        for char in s:
            if char not in cur:
                cur = ''.join([cur, char])
            else:
                cur = ''.join([cur[cur.index(char)+1:], char])
            if len(cur) > len(max_s):
                max_s = cur
        return len(max_s)

    def lengthOfLongestSubstring_hash(self, s: str) -> int:  # 80.32% 24.19%
        if len(s) <= 1:
            return len(s)
        chars = {}
        left = 0
        res = 0
        for right, char in enumerate(s):
            if char in chars:
                left = max(left, chars[char]+1)
            chars[char] = right
            res = max(res, right-left+1)
        return res
