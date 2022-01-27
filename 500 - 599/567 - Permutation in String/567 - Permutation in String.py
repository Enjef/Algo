class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:  # 6.42% 63.31%
        s_list = sorted(s1)
        k = len(s_list)
        for i in range(len(s2)-k+1):
            if s_list == sorted(s2[i:i+k]):
                return True
        return False

    def checkInclusion_v2(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        abc = 'abcdefghijklmnopqrstuvwxyz'
        s1_hash = {k:0 for k in abc}
        s2_hash = {k:0 for k in abc}
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

class Solution_ya_tarining_01_monster:  # 39.28% 64.10%

    def checkInclusion(self, s1: str, s2: str) -> bool:
        self.g, self.S = len(s1), len(s2)
        test = s1
        self.test_count = self.create_dict(test, self.g)
        self.tested = s2
        self.cur_count = self.create_dict(self.tested, self.g, True)
        self.same = 0
        self.same_count(self.test_count, self.cur_count)
        self.res = 0
        if self.same == len(self.test_count):
            self.res += 1
        if self.res:
            return True
        return self.compare()

    def create_dict(self, arr, idx, filled=False):
        new_dict = {}
        for char in arr[:idx]:
            if filled and char not in self.test_count:
                continue
            new_dict[char] = new_dict.get(char, 0) + 1
        return new_dict

    def same_count(self, dict1, dict2):
        for key in dict1:
            if key not in dict2:
                dict2[key] = 0
            else:
                if dict1[key] == dict2[key]:
                    self.same += 1

    def add_delete_el(self, el, shift):
        ans = 0
        if el in self.test_count and self.test_count[el] == self.cur_count[el]:
            ans -= 1
        self.cur_count[el] = self.cur_count.get(el, 0) + shift
        if el in self.test_count and self.test_count[el] == self.cur_count[el]:
            ans += 1
        return ans

    def compare(self):
        for i in range(self.g, self.S):
            new = self.tested[i]
            old = self.tested[i-self.g]
            self.same += self.add_delete_el(new, 1)
            self.same += self.add_delete_el(old, -1)
            self.res += int(self.same == len(self.test_count))
            if self.res:
                return True
        return bool(self.res)

class Solution_ya_training_01_refactored_v1:  # 59.65% 99.87%

    def checkInclusion(self, s1: str, s2: str) -> bool:
        def add_remove_char(old, new):
            res = 0
            if old in test and test[old] == 0:
                res -= 1
            if new in test and test[new] == 0:
                res -= 1
            if old in test:
                test[old] += 1
            if new in test:
                test[new] -= 1
            if old in test and test[old] == 0:
                res += 1
            if new in test and test[new] == 0:
                res += 1
            return res
        test = {}
        n = len(s1)
        for char in s1:
            test[char] = test.get(char, 0) + 1
        same = 0
        for char in s2[:n]:
            if char in test:
                if char in test and test[char] == 0:
                    same -= 1
                if char in test:
                    test[char] -= 1
                if char in test and test[char] == 0:
                    same += 1
        score = len(test)
        if same == score:
            return True
        for i in range(n, len(s2)):
            same += add_remove_char(s2[i-n], s2[i])
            if same == score:
                return True
        return same == score

class Solution_ya_training_01_refactored_v1:  # 60.11% 99.87%
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def add_remove_char(elem, shift):
            res = 0
            if elem in test and test[elem] == 0:
                res -= 1
            if elem in test:
                test[elem] += shift
            if elem in test and test[elem] == 0:
                res += 1
            return res
        test = {}
        n = len(s1)
        for char in s1:
            test[char] = test.get(char, 0) + 1
        same = 0
        for char in s2[:n]:
            same += add_remove_char(char, -1)
        score = len(test)
        if same == score:
            return True
        for i in range(n, len(s2)):
            same += add_remove_char(s2[i-n], 1) + add_remove_char(s2[i], -1)
            if same == score:
                return True
        return same == score
