class Solution:
    # 19.99% 59.43% (22.81% 59.43%)
    def longestContinuousSubstring(self, s: str) -> int:
        res = cur = 1
        n = len(s)
        for i in range(1, n):
            if ord(s[i]) - ord(s[i-1]) == 1:
                cur += 1
            else:
                cur = 1
            res = max(res, cur)
        return res

    def longestContinuousSubstring_best_speed(self, s: str) -> int:
        char_map = defaultdict()
        ss = string.ascii_lowercase
        i = 1
        for char in ss:
            if i < 26:
                char_map[char] = ss[i]
                i += 1
        ans = 1
        curr_len = 1
        prev = s[0]
        for c in s[1:]:
            if prev == 'z':
                curr_len = 1
                prev = c
                continue
            if c == char_map[prev]:
                curr_len += 1
                ans = max(ans, curr_len)
            else:
                curr_len = 1
            prev = c
        return ans

    def longestContinuousSubstring_2nd_best_speed(self, s: str) -> int:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        maxlen = 0
        for i in range(len(alphabet)):
            string = alphabet[i]
            j = i + 1
            l = string
            while string in s and j < len(alphabet):
                l = string
                string += alphabet[j]
                j += 1
                if j == len(alphabet) and string in s:
                    l = string
            if l in s:
                maxlen = max(len(l), maxlen)
        return maxlen

    def longestContinuousSubstring_best_memory(self, s: str) -> int:
        longest = 0 if len(s) == 0 else 1
        curr = 1
        for i in range(1, len(s)):
            if ord(s[i]) == ord(s[i - 1]) + 1:
                curr += 1
                longest = max(longest, curr)
            else:
                curr = 1
        return longest
