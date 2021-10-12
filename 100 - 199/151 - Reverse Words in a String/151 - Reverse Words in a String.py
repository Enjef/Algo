class Solution:
    def reverseWords(self, s: str) -> str:
        s = [x for x in s.split() if x != ' ']
        s.reverse()
        return ' '.join(s)