class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:  # 75.90% 80.36%
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

    def lengthOfLongestSubstring_mock(self, s: str) -> int:  # 21.95% 99.65%
        res = []
        cur = []
        for char in s:
            if char in cur:
                cur = cur[cur.index(char)+1:]
            cur.append(char)
            res = max([res, cur], key=len)
        return len(res)

    def lengthOfLongestSubstring_dict_left_right(
            self, s: str) -> int: # 85.22% 23.28%
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

    def lengthOfLongestSubstring_study_plan_day_6(
            self,
            s: str) -> int:  # 36.42% 54.61%
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

    def lengthOfLongestSubstring_best_speed(self, s: str) -> int:
        lengthOfLongestSubstring = 0
        currentSubstring = ''
        currentLength = 0
        index = 0
        for char in s:
            if char not in currentSubstring:
                currentSubstring += char
                currentLength = len(currentSubstring)
                if currentLength > lengthOfLongestSubstring:
                    lengthOfLongestSubstring = currentLength
            else:
                index = currentSubstring.find(char)
                currentSubstring += char
                currentSubstring = currentSubstring[index+1:]
        return lengthOfLongestSubstring
