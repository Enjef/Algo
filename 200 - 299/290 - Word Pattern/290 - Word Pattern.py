class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        char_map = {}
        s = s.split()
        if len(s) != len(pattern):
            return False
        for i in range(len(pattern)):
            if str(pattern[i]) not in char_map:
                if s[i] in list(char_map.values()):
                    return False
                char_map[str(pattern[i])] = s[i]
            elif char_map[str(pattern[i])] != s[i]:
                return False
        return True
