class Solution(object):
    def selfDividingNumbers(self, left, right):
        out = []
        for i in range(left, right + 1):
            sdn = True
            check = i
            if '0' in str(check):
                continue
            while check:
                if i % (check % 10) == 0:
                    check //= 10
                else:
                    sdn = False
                    break
            if sdn:
                out.append(i)
        return out
