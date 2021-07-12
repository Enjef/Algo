class Solution(object):
    def sumOddLengthSubarrays(self, arr):  # 30.96 % 69.25 %
        out = 0
        for i in range(1, len(arr)+1, 2):
            for j in range(0, len(arr)-i+1):
                out += sum(arr[j:j+i])
        return out
