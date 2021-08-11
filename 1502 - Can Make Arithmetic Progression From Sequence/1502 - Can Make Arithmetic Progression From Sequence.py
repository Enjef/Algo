class Solution:
    def canMakeArithmeticProgression(
            self,
            arr: List[int]) -> bool:  # 64.36% 34.79%
        arr.sort()
        return sum(
            [arr[0]-arr[1] != arr[i-1]-arr[i] for i in range(1, len(arr))]
        ) == 0

    def canMakeArithmeticProgression_best(self, arr: List[int]) -> bool:
        arr.sort()
        n = len(arr)
        prev = arr[1] - arr[0]
        for i in range(1, n - 1):
            diff = arr[i + 1] - arr[i]
            if diff != prev:
                return False
            prev = diff
        return True
