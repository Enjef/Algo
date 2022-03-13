class Solution:  # 60.70% 97.84%
    def plusOne(self, digits: List[int]) -> List[int]:
        return list(str(int(''.join(str(x) for x in digits))+1))
