class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        out = set()
        cur = ''
        for i in word:
            if cur and not i.isdigit():
                out.add(int(cur))
                cur = ''
            if i.isdigit():
                cur += i
        if cur:
            out.add(int(cur))
        return len(out)
