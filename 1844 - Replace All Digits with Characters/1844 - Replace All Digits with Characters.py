class Solution(object):

    def replaceDigits(self, s):  # 67.32%
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for i in range(len(s)):
            if s[i].isdigit():
                res += chr(int(s[i])+ord(s[i-1]))
            else:
                res += s[i]
        return res

    def replaceDigits_1(self, s):  # 17%
        out = ''
        for i in s:
            if i.isdigit():
                out += chr(ord(out[-1]) + int(i))
            else:
                out += i
        return out
