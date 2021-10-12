class Solution(object):
    def firstUniqChar(self, s):  #  60.72% 31.62%
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

    def firstUniqChar_sp_day_6(self, s: str) -> int:  # 12.73% 70.16%
        x_dict = {}
        for char in s:
            x_dict[char] = x_dict.get(char, 0) + 1
        for i, char in enumerate(s):
            if x_dict[char] == 1:
                return i
        return -1

    def firstUniqChar_best_speed(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        for item in "abcdefghijklmnopqrstuvwxyz":
            a = s.find(item)
            b = s.rfind(item)
            if a == b and a != -1:
                l = min(l, a)
        return l if l < len(s) else -1
