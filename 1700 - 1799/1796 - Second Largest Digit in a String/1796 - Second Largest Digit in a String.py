class Solution:
    def secondHighest(self, s: str) -> int:
        d_set = set()
        for i in s:
            if i.isdigit():
                d_set.add(i)
        if len(d_set) < 2:
            return -1
        d_set = sorted(list(d_set))
        return d_set[-2]
