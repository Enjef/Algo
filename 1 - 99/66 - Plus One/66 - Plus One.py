class Solution:
    def plusOne(self, digits):
        out = 1
        for i in range(len(digits)):
            out += digits[i] * 10 ** (len(digits) - i - 1)
            print(out)
        return [int(x) for x in (str(out))]


x = Solution()
print(x.plusOne([1, 2, 3]))
