class Solution:
    def countPrimes(self, n: int) -> int:
        n_list = list(range(2, n+1))
        for i in range(len(n_list)):
            if n_list[i] != 0:
                for j in range(i+n_list[i], len(n_list), n_list[i]):
                    n_list[j] = 0
            print(n_list)
        return len([x for x in n_list if x != 0])


x = Solution()
print(x.countPrimes(12))
