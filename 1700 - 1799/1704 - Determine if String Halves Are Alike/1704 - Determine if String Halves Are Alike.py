class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        count_a = 0
        count_b = 0
        for i in range(len(s) // 2):
            if s[i] in vowels:
                count_a += 1
            if s[i + len(s) // 2] in vowels:
                count_b += 1
        return count_a == count_b

    def halvesAreAlike_best(self, s: str) -> bool:  # best
        vow = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        mid = len(s)//2
        s1 = s[:mid]
        s2 = s[mid:]
        c1 = c2 = 0
        for i in vow:
            c1 += s1.count(i)
            c2 += s2.count(i)
        return c1 == c2
