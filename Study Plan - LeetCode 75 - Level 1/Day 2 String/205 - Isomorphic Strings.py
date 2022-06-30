class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = {}
        t_dict = {}
        for i in range(len(s)):
            if s[i] not in s_dict:
                s_dict[s[i]] = [i]
            else:
                s_dict[s[i]].append(i)
            if t[i] not in t_dict:
                t_dict[t[i]] = [i]
            else:
                t_dict[t[i]].append(i)
        if list(s_dict.values()) == list(t_dict.values()):
            return True
        return False
