class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        n_list = list(range(2, n))
        for i in range(int(len(n_list)**0.5)):
            if n_list[i]:
                n_list[n_list[i]*n_list[i]-2: len(n_list): n_list[i]] = [0] * len(range(n_list[i]*n_list[i]-2, len(n_list), n_list[i]))
        return len([x for x in n_list if x != 0])


x = Solution()
print(x.countPrimes(12))
