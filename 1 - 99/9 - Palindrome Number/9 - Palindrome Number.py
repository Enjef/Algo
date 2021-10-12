import math


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        if x < 0:
            return False
        i = 0
        j = int(math.log10(x))
        while i < j:
            if x // 10 ** j % 10 != x // 10 ** i % 10:
                return False
            i += 1
            j -= 1
        return True


x = Solution()
print(x.isPalindrome(0))
