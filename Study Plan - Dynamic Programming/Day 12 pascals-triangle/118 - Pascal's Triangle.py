class Solution:
    def generate(self, numRows: int) -> List[List[int]]:  # 70.23% 94.09%
        triangle = [[1]]
        level = 1
        while level < numRows:
            new_row = [1]
            for i in range(1, level):
                new_row.append(triangle[-1][i]+triangle[-1][i-1])
            new_row.append(1)
            triangle.append(new_row)
            level += 1
        return triangle
