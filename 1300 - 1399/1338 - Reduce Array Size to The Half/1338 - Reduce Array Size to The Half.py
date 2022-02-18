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
