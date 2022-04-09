class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:  # 81.52% 17.40%
        n = len(arr)
        arr.sort()
        for i, num in enumerate(arr):
            left, right = 0, n-1
            target = 2*num
            while left <= right:
                mid = left + (right-left)//2
                if mid != i and arr[mid] == target:
                    return True
                if arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
