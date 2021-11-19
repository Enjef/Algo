class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s = sorted(s)
        t = sorted(t)
        for i in range(len(s)):
            if s[-i] != t[-i]:
                return False
        return True

    def short(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def isAnagram_second_to_best(self, s: str, t: str) -> bool:
        for n in range(97, 123):
            if s.count(chr(n)) != t.count(chr(n)):
                return False
        return True

    def isAnagram_third_to_best(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

    def isAnagram_best_speed(self, s: str, t: str) -> bool:
        c1 = Counter(s)
        c2 = Counter(t)
        keys = set(c1.keys()).union(c2.keys())
        for key in keys:
            if key not in c1 or key not in c2 or c1[key] != c2[key]:
                return False
        return True

    def isAnagram_best_memory(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for letter in s:
            s_dict[letter] = s_dict.get(letter, 0) + 1
        for letter in t:
            t_dict[letter] = t_dict.get(letter, 0) + 1
        return s_dict == t_dict
