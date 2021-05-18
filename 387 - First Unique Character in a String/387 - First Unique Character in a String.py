class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        c_map = {}
        for i in range(len(s)):
            if s[i] not in c_map:
                c_map[s[i]] = i
            else:
                c_map[s[i]] = float('inf')
        return(min(list(c_map.values())) if
               min(list(c_map.values())) != float('inf') else -1
               )
