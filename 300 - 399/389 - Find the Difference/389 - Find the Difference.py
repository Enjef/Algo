class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s:
            return t
        for i in range(len(s)):
            t = t.replace(s[i], '', 1)
        return t
