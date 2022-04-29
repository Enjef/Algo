class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:  # 83.27% 97.77%
        def bin_search(row):
            left, right = 0, n - 1
            while left <= right:
                mid = (left+right)//2
                check_up = -1 if row == 0 else mat[row-1][mid]
                check_down = -1 if row == m-1 else mat[row+1][mid]
                check_left = -1 if mid == 0 else mat[row][mid-1]
                check_right = -1 if mid == n-1 else mat[row][mid+1]
                if (
                        check_left < mat[row][mid] > check_right and
                        check_up < mat[row][mid] > check_down):
                    return row, mid
                if check_left >= check_right:
                    right = mid - 1
                else:
                    left = mid + 1
            return None

        m, n = len(mat), len(mat[0])
        for i in range(m):
            res = bin_search(i)
            if res:
                return res
        return
