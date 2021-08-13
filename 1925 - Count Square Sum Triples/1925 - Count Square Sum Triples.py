class Solution:
    def countTriples(self, n: int) -> int:  # 67.36% 52.48%
        out = 0
        for x in range(1, n+1):
            for y in range(x+1, n+1):
                z = (x*x + y*y)**(1/2)
                if z > n:
                    break
                if z % 1 == 0:
                    out += 2
        return out
