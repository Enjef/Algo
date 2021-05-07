class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        n_list = list(range(2, n))
        for i in range(len(n_list)):
            if n_list[i] != 0:
                for j in range(i+n_list[i], len(n_list), n_list[i]):
                    n_list[j] = 0
        return len([x for x in n_list if x != 0])


x = Solution()
print(x.countPrimes(12))
