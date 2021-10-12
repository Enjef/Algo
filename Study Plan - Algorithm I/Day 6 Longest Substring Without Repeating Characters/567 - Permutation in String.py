class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s_list = sorted(s1)
        k = len(s_list)
        for i in range(len(s2)-k+1):
            if s_list == sorted(s2[i:i+k]):
                return True
        return False

    def checkInclusion_hash(self, s1: str, s2: str) -> bool:  # 99.99% 33.41%
        if len(s1) > len(s2):
            return False
        abc = 'abcdefghijklmnopqrstuvwxyz'
        s1_hash = {k: 0 for k in abc}
        s2_hash = {k: 0 for k in abc}
        for char in s1:
            s1_hash[char] = s1_hash.get(char, 0) + 1
        for i in range(len(s1)):
            s2_hash[s2[i]] = s2_hash.get(s2[i], 0) + 1
        if s1_hash == s2_hash:
            return True
        n = len(s1)
        for i in range(n, len(s2)):
            s2_hash[s2[i-n]] -= 1
            s2_hash[s2[i]] += 1
            if s1_hash == s2_hash:
                return True
        return False
