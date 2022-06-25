class Solution:
    def countAsterisks(self, s: str) -> int:
        return sum(x.count('*') for x in [sub for i, sub in enumerate(s.split('|')) if not i % 2])

    def countAsterisks_v2(self, s: str) -> int:
        return sum([a.count('*') for a in s.split('|')][0::2])
