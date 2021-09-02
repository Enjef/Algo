class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
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
