class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:  # 21.54% 83.79%
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = zip(*matrix[::-1])
        return
