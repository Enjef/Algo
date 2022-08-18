class Solution:
    def minSetSize(self, arr: List[int]) -> int:  # 65.87% 49.85%
        counter = {}
        for num in arr:
            counter[num] = counter.get(num, 0) + 1
        cur = 0
        target = len(arr) // 2
        for i, qty in enumerate(sorted(counter.values(), reverse=True)):
            cur += qty
            if cur >= target:
                return i+1
        return 1

    # 81.83% 52.99% (46.63% 52.73%)
    def minSetSize_v2(self, arr: List[int]) -> int:
        counter = {}
        for num in arr:
            counter[num] = counter.get(num, 0) + 1
        target = len(arr) // 2
        counts = sorted(counter.values(), reverse=True)
        for i in range(1, len(counts)):
            counts[i] += counts[i-1]
        left, right = 0, len(counts)-1
        while left < right:
            mid = (left + right) // 2
            if counts[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return 1 if right == 0 else right+1

    # 77.00% 53.88% (19.18% 57.69%)
    def minSetSize_v3(self, arr: List[int]) -> int:
        counter = Counter(arr)
        target = len(arr) // 2
        counts = sorted(counter.values(), reverse=True)
        for i in range(1, len(counts)):
            counts[i] += counts[i-1]
        idx = bisect_left(counts, target)
        return idx+1

    # 58.70% 53.88%
    def minSetSize_v4(self, arr: List[int]) -> int:
        return (target:=len(arr)//2, prev:=0, arr:=sorted(Counter(arr).values(), reverse=True), bisect_left([prev:=prev+x for x in arr], target))[3] + 1

    # 35.83% 78.40% (43.71% 54.13%)
    def minSetSize_v5(self, arr: List[int]) -> int:
        return (target:=len(arr)//2, prev:=0, bisect_left([prev:=prev+x for x in sorted(Counter(arr).values(), reverse=True)], target))[2] + 1

    # 30.75% 67.22%
    def minSetSize_v6(self, arr: List[int]) -> int:
        counts = sorted(Counter(arr).values(), reverse=True)
        for i in range(1, len(counts)):
            counts[i] += counts[i-1]
        return bisect_left(counts, len(arr)//2)+1

    def minSetSize_best_speed(self, A):
        C = list(Counter(A).values())
        C.sort()
        n = len(A)
        lim = n*0.5
        result = 0
        while n > lim:
            n -= C.pop()
            result += 1
        return result

    def minSetSize_2nd_best_speed(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        frequencies = list(cnt.values())
        frequencies.sort()

        ans, removed, half = 0, 0, len(arr) // 2
        while removed < half:
            ans += 1
            removed += frequencies.pop()
        return ans

    def minSetSize_best_memory(self, arr: List[int]) -> int:
        arr.sort()
        count = []
        tmp = 1
        for i in range (1, len(arr)):
            if arr[i] > arr[i - 1]:
                count.append(tmp)
                tmp = 1
            else:
                tmp +=1
        count.append(tmp)
        count.sort()
        current = 0
        target = len(arr) // 2 + len(arr) % 2
        sets_to_remove = 0
        while current < target:
            current += count.pop()
            sets_to_remove += 1
        return sets_to_remove
