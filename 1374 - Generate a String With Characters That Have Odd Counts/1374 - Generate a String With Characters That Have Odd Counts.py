class Solution:
    def generateTheString(self, n: int) -> str:  # 60.34% 66.28%
        if n == 1:
            return 'a'
        if n % 2 == 0:
            first = 'a'
        else:
            first = 'ab'
        second = 'c'*(n-len(first))
        return ''.join([first, second])

    def generateTheString_best(self, n: int) -> str:
        if n % 2 == 0:
            return 'a' + ('b' * (n - 1))
        return 'a' * n
