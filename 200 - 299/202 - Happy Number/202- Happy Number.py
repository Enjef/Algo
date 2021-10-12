class Solution:
    def isHappy(self, n: int) -> bool:
        if n in [1, 7]:
            return True
        if n in [0, 2, 3, 4, 5, 6, 8, 9]:
            return False
        sum = 0
        for num in str(n):
            sum += int(num)*int(num)
        return self.isHappy(sum)
