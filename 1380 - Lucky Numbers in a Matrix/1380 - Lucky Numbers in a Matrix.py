class Solution:
    def luckyNumbers(
            self,
            matrix: List[List[int]]) -> List[int]:  # 96.69% 38.62%
        cols = [max(x) for x in zip(*matrix)]
        rows = [min(x) for x in matrix]
        return list(set(cols) & set(rows))

    def luckyNumbers_best_memory(self, matrix: List[List[int]]) -> List[int]:
        minRows = set()
        maxCols = set()
        for row in matrix:
            minRows.add(min(row))
        for col in range(len(matrix[0])):
            maxCols.add(max(matrix[i][col] for i in range(len(matrix))))
        return list(minRows.intersection(maxCols))
