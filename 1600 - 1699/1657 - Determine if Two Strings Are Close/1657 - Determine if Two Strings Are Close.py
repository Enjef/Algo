class Solution:
    # 28.00% 80.00% (28.80% 68.80%)
    def closeStrings(self, word1: str, word2: str) -> bool:
        first, second = Counter(word1), Counter(word2)
        return set(word1) == set(word2) and sorted(first.values()) == sorted(second.values())

    # 32.00% 43.60% (29.60% 43.60%)
    def closeStrings_v2(self, word1: str, word2: str) -> bool:
        return set(word1) == set(word2) and sorted(Counter(word1).values()) == sorted(Counter(word2).values())

    # 90.00% 68.80% (45.60% 16.80%)
    def closeStrings_3(self, word1: str, word2: str) -> bool:
        first, second = Counter(word1), Counter(word2)
        return first.keys() == second.keys() and sorted(first.values()) == sorted(second.values())

    # 84.80% 43.60% (34.80% 94.00%)
    def closeStrings_v4(self, word1: str, word2: str) -> bool:
        first, second = Counter(word1), Counter(word2)
        return first.keys() == second.keys() and Counter(first.values()) == Counter(second.values())


class Solution_best_speed:
    def closeStrings(self, word1: str, word2: str) -> bool:
        n1 = len(word1)
        n2 = len(word2)
        if n1 != n2:
            return False
        w1 = set(word1)
        w2 = set(word2)
        if w1 != w2:
            return False
        n = len(w1)
        arr1 = [0]*n
        arr2 = [0]*n
        c1 = 0
        c2 = 0
        for i in w1:
            arr1[c1] = word1.count(i)
            c1 += 1
        for j in w2:
            arr2[c2] = word2.count(j)
            c2 += 1
        arr1.sort()
        arr2.sort()
        if arr1 == arr2:
            return True
        else:
            return False

    def closeStrings_2nd(self, word1: str, word2: str) -> bool:
        return set(word1) == set(word2) and Counter(Counter(word1).values()) == Counter(Counter(word2).values())


class Solution_best_memory:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        cm1 = Counter(word1)
        cm2 = Counter(word2)
        keys1 = sorted(cm1.keys())
        keys2 = sorted(cm2.keys())
        values1 = sorted(cm1.values())
        values2 = sorted(cm2.values())
        if keys1 != keys2:
            return False
        if values1 != values2:
            return False
        return True

    def closeStrings_2nd(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        d1 = Counter(word1)
        d2 = Counter(word2)
        return set(word1) == set(word2) and Counter(d1.values()) == Counter(d2.values())
