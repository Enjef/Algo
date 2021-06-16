class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        s = {}
        for word in words:
            for char in word:
                if char not in s:
                    s[char] = 1
                else:
                    s[char] += 1
        for char in s:
            if s[char] % len(words) != 0:
                return False
        return True
