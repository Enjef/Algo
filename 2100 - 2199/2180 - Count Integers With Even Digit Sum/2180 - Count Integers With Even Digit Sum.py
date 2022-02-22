class Solution:
    def countEven(self, num: int) -> int:  # 6.31% 60.68%
        count = 0
        for prev_num in range(1, num+1):
            if not sum([int(char) for char in str(prev_num)]) % 2:
                count += 1
        return count

    def countEven_best_speed(self, num: int) -> int:
        div, mod = divmod(num, 10)
        count = div * 5
        odd = True if div & 1 else False
        while div:
            div //= 10
            if div & 1:
                odd = not odd
        if odd:
            count += sum(1 for i in range(1, mod+1, 2))
        else:
            count += sum(1 for i in range(0, mod+1, 2))
        return count - 1

    def countEven_2nd_best_speed(self, num: int) -> int:
        def s(n):
            curr = 0
            while n > 0:
                curr = curr+n % 10
                n = n//10
            return curr
        if s(num) % 2:
            return (num-1)//2
        else:
            return num//2

    def countEven_best_memory(self, num: int) -> int:
        count = 0
        for i in range(1, num+1):
            if sum([int(x) for x in str(i)]) % 2 == 0:
                count += 1
        return count
