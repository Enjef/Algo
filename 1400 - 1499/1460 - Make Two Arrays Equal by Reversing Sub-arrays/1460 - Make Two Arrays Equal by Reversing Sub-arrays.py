class Solution:
    def canBeEqual(
            self,
            target: List[int],
            arr: List[int]) -> bool:  # 80.81% 32.45%
        target.sort()
        arr.sort()
        if target == arr:
            return True
        return False

    def canBeEqual_best(self, target: List[int], arr: List[int]) -> bool:
        if sorted(target) == sorted(arr):
            return True
        else:
            return False
