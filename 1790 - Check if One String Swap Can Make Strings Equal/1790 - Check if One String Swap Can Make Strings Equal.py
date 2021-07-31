class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:  # 5.43% 93.60%
        if s1 == s2:
            return True
        return self.helper(s1, s2) or self.helper(s2, s1)

    def helper(self, string, target):
        for i in range(len(string)):
            for j in range(i, len(string)):
                if ''.join(
                    [
                        string[:i], string[j],
                        string[i+1:j], string[i], string[j+1:]]
                        ) == target:
                    return True
        return False

    def areAlmostEqual_s_best(self, s1: str, s2: str) -> bool:
        a1, a2 = [], []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                a1.append(s1[i])
                a2.append(s2[i])
        if len(a1) > 0:
            return len(a1) == 2 and a1[0] == a2[1] and a1[1] == a2[0]
        return True
