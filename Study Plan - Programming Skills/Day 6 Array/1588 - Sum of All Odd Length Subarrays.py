class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:  # 69.27% 81.26%
        out = sum(arr)
        n = len(arr)
        win = 3
        while win <= n+1:
            for i in range(n-win+1):
                out += sum(arr[i:i+win])
            win += 2
        return out
