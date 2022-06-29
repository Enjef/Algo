class Solution:
    def greatestLetter(self, s: str) -> str:  # 53.74% 70.76%
        d = defaultdict(set)
        for char in s:
            d[char.upper()].add(char)
        return max(x if len(y) == 2 else '' for x, y in d.items())

    def greatestLetter(self, s: str) -> str:  # 85.17% 28.98%
        arr = [0] * 26
        set_s = set(s)
        for char in set_s:
            arr[ord(char.upper())-ord('A')] += 1
        for i in range(25, -1, -1):
            if arr[i] == 2:
                return chr(ord('A')+i)
        return ''

    def greatestLetter_best_speed(self, s: str) -> str:
        ans = ''
        s = set(s)
        for char in ascii_lowercase:
            if char in s and char.upper() in s:
                ans = char.upper()
        return ans

    def greatestLetter_2nd_best_speed(self, s: str) -> str:
        seen = set()
        for char in s:
            seen.add(char)
        ans = ''
        for i in range(26):
            lower = chr(ord("a") + i)
            upper = chr(ord("A") + i)
            if lower in seen and upper in seen:
                ans = max(ans, upper)
        return ans

    def greatestLetter_best_memory(self, s: str) -> str:
        for char in reversed(ascii_uppercase):
            char_l = char.lower()
            if char in s and char_l in s:
                return char
        return ''
