class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s_list = sorted(s1)
        k = len(s_list)
        for i in range(len(s2)-k+1):
            if s_list == sorted(s2[i:i+k]):
                return True
        return False
