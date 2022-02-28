class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool: # 94.51% 58.84%
        if s1 == s2:
            return True
        diff = None
        found = False
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if diff:
                    if found:
                        return False
                    if [s1[i], s2[i]] == diff:
                        found = True
                    else:
                        return False
                else:
                    diff = [s2[i], s1[i]]
        return found
