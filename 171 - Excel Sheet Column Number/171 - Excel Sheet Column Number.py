class Solution:
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        out = 0
        for i, char in enumerate(columnTitle):
            out += (abc.index(char) + 1) * (26**(len(columnTitle)-i-1))
        return out
