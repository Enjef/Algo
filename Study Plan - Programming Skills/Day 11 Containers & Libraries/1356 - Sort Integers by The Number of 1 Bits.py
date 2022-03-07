class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:  # 98.51% 40.87%
        def weight(num):
            return (str(bin(num)).count('1'), num)
        return sorted(arr, key=weight)
