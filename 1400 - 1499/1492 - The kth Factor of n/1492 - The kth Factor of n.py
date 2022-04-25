class Solution:
    def kthFactor(self, n: int, k: int) -> int:  # 96.74% 17.82%
        count = 0
        for num in range(1, n+1):
            if n % num == 0:
                count += 1
            if count == k:
                return num
        return -1

    def kthFactor_best_speed(self, n: int, k: int) -> int:
        factor = []
        sqrtN = int(n**0.5)
        for i in range(1, sqrtN+1):
            if n % i == 0:
                k -= 1
                factor.append(i)
                if k == 0:
                    return i
        if sqrtN * sqrtN == n:
            k += 1
        length = len(factor)
        return n//factor[length-k] if k <= length else -1

    def kthFactor_2nd_best_speed(self, n: int, k: int) -> int:
        heap = []

        def push(num):
            heappush(heap, -num)
            if (len(heap) > k):
                heappop(heap)

        for x in range(1, int(n ** 0.5) + 1):
            if n % x == 0:
                push(x)
                if x != n // x:
                    push(n // x)
        return -heappop(heap) if k == len(heap) else -1

    def kthFactor_best_memory(self, n: int, k: int) -> int:
        ranges = [num for num in range(1, n + 1) if n % num == 0]
        try:
            return ranges[k-1]
        except IndexError:
            return -1
