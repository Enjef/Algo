class Solution(object):
    def sumOddLengthSubarrays(self, arr):  # 30.96 % 69.25 %
        out = 0
        for i in range(1, len(arr)+1, 2):
            for j in range(0, len(arr)-i+1):
                out += sum(arr[j:j+i])
        return out

    def sumOddLengthSubarrays_v2(self, arr: List[int]) -> int:  # 69.27% 81.26%
        out = sum(arr)
        n = len(arr)
        win = 3
        while win <= n+1:
            for i in range(n-win+1):
                out += sum(arr[i:i+win])
            win += 2
        return out

    def sumOddLengthSubarrays_best_speed(self, arr: List[int]) -> int:
        n = len(arr)
        s = 0
        freq = 0
        n = len(arr)
        for i in range(n):
            freq = freq - (i + 1) // 2 + (n - i + 1) // 2
            s += freq*arr[i]
        return s

    def sumOddLengthSubarrays_best_memory(self, arr: List[int]) -> int:
        ans=0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)+1):
                t=arr[i:j]
                if len(t)%2!=0:
                    ans+=sum(t)
        return ans
