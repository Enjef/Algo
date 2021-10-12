class Solution(object):
    def numberOfMatches(self, n):
        out = 0
        if n < 2:
            return out
        while n != 2:
            k = 0
            if n % 2 != 0:
                k = 1
            n //= 2
            out += n
            n += k

        return out + 1
