class Solution:
    def reverseWords(self, s: str) -> str:
        s = [x for x in s.split() if x != ' ']
        s.reverse()
        return ' '.join(s)

    # 83.70% 16.15%
    def reverseWords_v2(self, s: str) -> str:
        return ' '.join(reversed([x for x in s.split() if x]))


class Solution_best_split:
    def reverseWords_1st(self, s: str) -> str:
        return ' '.join(reversed(s.split()))

    def reverseWords_2nd(self, s: str) -> str:
        return ' '.join(s.split()[::-1])


class Solution_best_memory:
    def reverseWords(self, s: str) -> str:
        ans = ''
        i = 0
        word = ''
        while i < len(s):
            if s[i] != ' ':
                word += s[i]
            elif word != '':
                ans = word + ' ' + ans
                word = ''
            i += 1
        if word != '':
            ans = word + ' ' + ans
        return ans.strip()

    def reverseWords_2nd(self, s: str) -> str:
        return ' '.join(s.split()[::-1])
