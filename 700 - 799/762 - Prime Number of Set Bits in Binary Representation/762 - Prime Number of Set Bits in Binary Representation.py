class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:  # 69.19% 29.55%
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        return sum(
            [str(bin(x)).count('1') in primes for x in range(left, right+1)])

    def countPrimeSetBits_2nd_best_speed(self, left: int, right: int) -> int:
        prime_numbers = set([2, 3, 5, 7, 11, 13, 17, 19])
        ans = 0
        for i in range(left, right + 1):
            if i.bit_count() in prime_numbers:
                ans += 1
        return ans

    def countPrimeSetBits_3d_best_speed(self, left: int, right: int) -> int:
        def isPrime(n):
            if n == 1:
                return False
            if n == 2:
                return True
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True
        cnt = 0
        mem = {}
        for num in range(left, right + 1):
            bit_cnt = num.bit_count()
            if bit_cnt not in mem:
                mem[bit_cnt] = isPrime(bit_cnt)
            if mem[bit_cnt]:
                cnt += 1
        return cnt

    def countPrimeSetBits(self, left: int, right: int) -> int:
        def isPrime(x):
            if x == 2 or x == 3 or x == 5 or x == 7 or x == 11 or x == 13 or x == 17 or x == 19:
                return True

            return False
        c = 0
        for b in range(left, right + 1):
            if isPrime(bin(b)[2:].count("1")):
                c += 1
        return c
