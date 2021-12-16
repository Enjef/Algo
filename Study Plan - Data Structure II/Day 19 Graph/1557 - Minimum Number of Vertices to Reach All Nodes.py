class Solution:
    def findSmallestSetOfVertices(
            self,
            n: int,
            edges: List[List[int]]) -> List[int]:  # 30.93% 26.35%
        nodes = set(range(n))
        visited = set()
        for x, y in edges:
            visited.add(y)
        return nodes - visited
