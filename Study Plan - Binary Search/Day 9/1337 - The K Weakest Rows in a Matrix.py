class Solution:
    def kWeakestRows(self, mat, k):  # 99.77% 90.09%
        arr = []
        heapify(arr)
        for i in range(len(mat)):
            left, right = 0, len(mat[0])-1
            while left <= right:
                mid = left + (right-left)//2
                if mat[i][mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            if left != -1:
                heappush(arr, (left, i))
        return [x[1] for x in sorted(arr)[:k]]
