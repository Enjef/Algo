class Solution:
    def digitCount(self, num: str) -> bool:
        d = {x: 0 for x in range(10)}
        for char in num:
            d[int(char)] += 1
        for i, el in enumerate(num):
            if d[i] != int(el):
                return False
        return True
