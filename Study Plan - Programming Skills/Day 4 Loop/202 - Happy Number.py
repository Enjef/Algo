class Solution:
    def isHappy(self, n: int) -> bool: # 69.08% 82.95%
        seen = set()
        while True:
            n = sum([int(x)*int(x) for x in str(n)])
            if n in seen:
                return False
            if n == 1:
                return True
            seen.add(n)
