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

    def findSmallestSetOfVertices_best_speed(
            self, n: int, edges: List[List[int]]) -> List[int]:
        indegrees = [0] * n
        for _, end in edges:
            indegrees[end] += 1
        return [i for i, v in enumerate(indegrees) if v == 0]

    def findSmallestSetOfVertices_best_memory(
            self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [0] * n 
        for e in edges:
            indegree[e[1]] += 1
        ret = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                ret.append(i)
        return ret
