class Solution:
    def isThree(self, n: int) -> bool:  # 48.72% 72.88%
        count = 2
        for i in range(2, n):
            if n % i == 0:
                count += 1
        return count == 3

    def isThree_best(self, n: int) -> bool:
        if n == 1 or n == 2 or n == 3:
            return False
        root = math.floor(math.sqrt(n))
        if root**2 != n:
            return False
        else:
            for i in range(2, root//2):
                if n % i == 0:
                    return False
        return True
