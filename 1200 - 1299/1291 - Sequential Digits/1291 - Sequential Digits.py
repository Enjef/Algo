class Solution:
    def sequentialDigits(
            self, low: int, high: int) -> List[int]:  #  95.17% 23.79%
        digits = '123456789'
        out = []
        for i in range(len(str(low)), len(str(high)) + 1):
            for j in range(0, 10 - i):
                cur = int(digits[j: j + i])
                if cur >= low and cur <= high:
                    out.append(cur)
        return out

    def sequentialDigits_best_speed(self, low: int, high: int) -> List[int]:
        sample = "123456789"
        n = 10
        nums = []
        for length in range(len(str(low)), len(str(high)) + 1):
            for start in range(n - length):
                num = int(sample[start: start + length])
                if num >= low and num <= high:
                    nums.append(num)
        return nums

    def sequentialDigits_2nd_best_speed(self, low: int, high: int) -> List[int]:
        out = []
        queue = deque(range(1,10))
        while queue:
            elem = queue.popleft()
            if low <= elem <= high:
                out.append(elem)
            elif elem > high:
                break
            last = elem % 10
            if last < 9:
                queue.append(elem*10 + last + 1)
        return out

    def sequentialDigits_best_memory(self, low: int, high: int) -> List[int]:
        l = len(str(low))
        h = len(str(high))
        
        def gen(n):
            v = []
            for i in range(0, 10-n):
                v_ = int(''.join(str(j+i) for j in range(1, n+1)))
                if low <= v_ <= high:
                    v.append(v_)
                if v_ > high:
                    break
            return v
        
        ans = []
        for n in range(l, h+1):
            ans.extend(gen(n))
        return ans
