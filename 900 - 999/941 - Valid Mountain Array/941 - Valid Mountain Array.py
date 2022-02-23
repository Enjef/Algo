class Solution:
    def validMountainArray(self, arr: List[int]) -> bool: #  69.17% 79.42%
        if len(arr) < 3:
            return False
        up = False
        down = False
        index_max = arr.index(max(arr))
        for i in range(1, len(arr)):
            if arr[i-1] == arr[i]:
                return False
            if arr[i-1] > arr[i] and i <= index_max:
                return False
            if arr[i-1] < arr[i] and i > index_max:
                return False
            if arr[i-1] > arr[i]:
                down = True
            if arr[i-1] < arr[i]:
                up = True
        return up and down

    def validMountainArray_mock(self, arr: List[int]) -> bool: # 68.47% 94.84%
        if len(arr) < 3:
            return False
        if arr[0] >= arr[1]:
            return False
        up = True
        for i in range(1, len(arr)):
            if up:
                if arr[i] > arr[i-1]:
                    continue
                elif arr[i] < arr[i-1]:
                    up = False
                else:
                    return False
            else:
                if arr[i] < arr[i-1]:
                    continue
                return False
        return not up

    def validMountainArray_best_speed(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        pivot = -1
        prev = float('-inf')
        for i, cur in enumerate(arr):
            if cur == prev:
                return False
            elif pivot < 0 and cur < prev:
                pivot = i - 1
            elif pivot >= 0 and cur > prev:
                return False
            prev = cur
        return pivot > 0 and pivot < len(arr) - 1

    def validMountainArray_2nd_best_speed(self, arr: List[int]) -> bool:
        m = max(arr)
        mi = arr.index(m)
        a = arr[:mi+1]
        b = arr[mi:]
        
        return (
            len(a) > 1 and len(b) > 1 and
            a == sorted(a) and b == sorted(b, reverse=True) and
            len(a) == len(set(a)) and len(b) == len(set(b))
        )
