class Solution:
    def canMakeArithmeticProgression(self, arr) -> bool:  # 64.36% 34.79%
        arr.sort()
        return sum(
            [arr[0]-arr[1] != arr[i-1]-arr[i] for i in range(1, len(arr))]
        ) == 0

    def canMakeArithmeticProgression_best_speed(self, arr: List[int]) -> bool:
        m = min(arr)
        gap = (max(arr) - m) / (len(arr) - 1)
        if gap == 0:
            return True
        s = set(num - m for num in arr)
        return len(s) == len(arr) and all(diff % gap == 0 for diff in s)

    def canMakeArithmeticProgression_2nd_best_speed(self, arr) -> bool:
        newArr = sorted(arr)
        diff = newArr[0] - newArr[1]
        for i in range(2, len(newArr)):
            if diff != newArr[i - 1] - newArr[i]:
                return False
        return True

    def canMakeArithmeticProgression_best_memory(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        return all(diff == arr[i] - arr[i-1] for i in range(2, len(arr)))
