class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        switch = 1
        index = 0
        out = ['' for _ in range(numRows)]
        for i in range(len(s)):
            out[index] += s[i]
            index += switch
            if index == numRows - 1 or index == 0:
                switch *= -1
        out = ''.join(out)
        return out


x = Solution()
x.convert('PAYPALISHIRING', 4)
