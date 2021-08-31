class Solution:
    def reverseWords(self, s: str) -> str:
        temp = s.split()
        for i, word in enumerate(temp):
            temp[i] = word[::-1]
        return ' '.join(temp)
