class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:  # 6.42% 63.31%
        s_list = sorted(s1)
        k = len(s_list)
        for i in range(len(s2)-k+1):
            if s_list == sorted(s2[i:i+k]):
                return True
        return False

    def checkInclusion_best_speed(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        dict1 = {i: 0 for i in set(s2)}
        dict2 = {}
        dict2.update(dict1)
        dict1.update({i: s1.count(i) for i in set(s1)})
        ls1 = len(s1)
        ls2 = len(s2)
        dict2.update({i: s2[:ls1].count(i) for i in set(s2[:ls1])})
        if dict1 == dict2:
            return True
        right = ls1
        left = 0
        while right < ls2:
            dict2[s2[right]] += 1
            dict2[s2[left]] -= 1
            if dict1 == dict2:
                return True
            right += 1
            left += 1
        return False

    def checkInclusion_sec_to_best_memory(self, s1: str, s2: str) -> bool:
        wlen = len(s1)
        l, r = 0, wlen
        while r <= len(s2):
            uncommon = [x for x in set(s1) if s1.count(x) != s2[l:r].count(x)]
            if len(uncommon) == 0:
                return True
            l += 1
            r += 1
        return False
