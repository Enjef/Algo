class Solution:
    def largestOddNumber(self, num: str) -> str:  # 43.21% 54.72%
        for i in range(len(num)-1, -1, -1):
            if num[i] in ['1', '3', '5', '7', '9']:
                return num[:i+1]
        return ''
