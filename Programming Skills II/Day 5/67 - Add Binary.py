class Solution:
    def addBinary(self, a: str, b: str) -> str:  # 37.59% 45.16%
        n, m = len(a), len(b)
        if n < m:
            a = '0'*(m-n) + a
        else:
            b = '0'*(n-m) + b
        extra = False
        result = []
        for i in range(len(a)-1, -1, -1):
            cur = int(a[i]) + int(b[i])
            if cur == 0:
                if extra:
                    result.append('1')
                    extra = False
                else:
                    result.append('0')
            elif cur == 1:
                if extra:
                    result.append('0')
                    extra = True
                else:
                    result.append('1')  
            else:
                if extra:
                    result.append('1')
                    extra = True
                else:
                    result.append('0')
                    extra = True
        if extra:
            result.append('1')
        return ''.join(result)[::-1]

    def addBinary_v2(self, a: str, b: str) -> str:  # 59.21% 82.99%
        return str(bin(int(a, 2)+int(b, 2)))[2:]
