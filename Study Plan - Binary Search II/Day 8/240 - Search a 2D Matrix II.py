class Solution:
    def searchMatrix(self, matrix, target):  # 97.57% 86.91%
        def bin_search(arr):
            left = 0
            right = len(matrix[0])-1
            while left <= right:
                mid = (left+right)//2
                if arr[mid] == target:
                    return target
                if arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return arr[right]
        
        for row in matrix:
            if bin_search(row) == target:
                return True
        return False
