class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return (
            'abcdefgh'.index(coordinates[0]) + 1 + int(coordinates[1])
        ) % 2 != 0

    def squareIsWhite_best(self, coordinates: str) -> bool: # 97 or  ord("a")
        return ((ord(coordinates[0]) - 97 + int(coordinates[1])) % 2 == 0)
