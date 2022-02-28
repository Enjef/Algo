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

    def areAlmostEqual_sp_day4(self, s1: str, s2: str):  # 94.51% 58.84%
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

    def areAlmostEqual_s_best(self, s1: str, s2: str) -> bool:
        a1, a2 = [], []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                a1.append(s1[i])
                a2.append(s2[i])
        if len(a1) > 0:
            return len(a1) == 2 and a1[0] == a2[1] and a1[1] == a2[0]
        return True

    def areAlmostEqual_best_speed(self, s1: str, s2: str) -> bool:
        count = 0
        p = ''
        d1 = {}
        d2 = {}
        for x in s1:
            d1[x] = d1.get(x, 0)+1
        for y in s2:
            d2[y] = d2.get(y, 0)+1
        for z in d1:
            if d1[z] != d2.get(z, 0):
                return False
        for z1 in d2:
            if d2[z1] != d1.get(z1, 0):
                return False
        for i, j in enumerate(s1):
            if j != s2[i]:
                count += 1
                p = p+j+s2[i]
        if count == 0:
            return True
        elif count == 2 and len(set(p)) == 2:
            return True
        return False

    def areAlmostEqual_2nd_best_speed(self, s1: str, s2: str) -> bool:
        buf = []
        for i, (c1, c2) in enumerate(zip(s1, s2)):
            if c1 != c2:
                buf.append(i)
                if len(buf) > 2:
                    return False
        if (len(buf) == 0 
            or len(buf) == 2 
            and (
                s1[buf[0]] == s2[buf[1]] 
                and s2[buf[0]] == s1[buf[1]] 
            )):
            return True
        return False

    def areAlmostEqual(self, s1: str, s2: str) -> bool:        
        if sorted(s1) != sorted(s2):
            return False
        diff_counter = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff_counter += 1
        return diff_counter == 2 or diff_counter == 0
