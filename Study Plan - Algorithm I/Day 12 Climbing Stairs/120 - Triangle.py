class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:  # 58.47% 50.85%
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    triangle[i][j] += triangle[i-1][0]
                elif j == len(triangle[i]) - 1:
                    triangle[i][j] += triangle[i-1][i-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j], triangle[i-1][j-1])
        return min(triangle[-1])
