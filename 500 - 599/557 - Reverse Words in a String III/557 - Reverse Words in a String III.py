class Solution:
    def reverseWords(self, s):
        s = s.split()
        for i in range(len(s)):
            s[i] = s[i][::-1]
        s = ' '.join(s)
        return s
