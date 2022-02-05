class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:  # 32.98% 82.98%
        n = len(arr)
        out = []
        for i in range(n):
            idx = arr[:n-i].index(max(arr[:n-i]))
            if idx == n-i-1:
                continue
            out.extend([idx+1, n-i])
            arr[:idx+1] = arr[:idx+1][::-1]
            arr[:n-i] = arr[:n-i][::-1]
        return out

    def pancakeSort_best_speed(self, A: List[int]) -> List[int]:
        result, n = [], len(A)
        for i in range(n, 0, -1):
            pl = A.index(i)
            if pl == i-1:
                continue
            if pl != 0:
                result.append(pl+1)
                A[:pl+1] = A[:pl+1][::-1]
            result.append(i)
            A[:i] = A[:i][::-1]
        return result

    def pancakeSort_best_memoty(self, arr: List[int]) -> List[int]:
        klist = []
        for i in reversed(range(len(arr))):
            k = arr.index(min(arr[:i+1])) + 1
            klist.append(k)
            self.flip(arr, k)
            self.flip(arr, i+1)
            klist.append(i+1)
        klist.append(len(arr))
        return klist

    def flip(self, arr, k):
        left, right = 0, k-1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
