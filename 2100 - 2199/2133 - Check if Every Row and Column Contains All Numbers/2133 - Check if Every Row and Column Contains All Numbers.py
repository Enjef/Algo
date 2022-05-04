class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:  # 25.61% 85.70%
        target = set(range(1, len(matrix)+1))
        return (
            all([set(row)==target for row in matrix]) and
            all([set(col)==target for col in zip(*matrix)])
        )

    def checkValid_best_speed(self, matrix: List[List[int]]) -> bool:
        return all( len(set(z)) == len(matrix) for z in matrix ) \
                and all( len(set(z)) == len(matrix) for z in zip(*matrix) )
