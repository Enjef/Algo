class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:  # 20.00% 40.00%
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (
                    not grid[i][j] and (i == j or (len(grid[0])-i-1) == j) or
                    grid[i][j] and not (i == j or (len(grid[0])-i-1) == j)):
                        return False
        return True

    def checkXMatrix_best_speed(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if (i == j or i+j == n-1) and not grid[i][j] or i != j and i+j != n-1 and grid[i][j]:
                    return False
        return True
