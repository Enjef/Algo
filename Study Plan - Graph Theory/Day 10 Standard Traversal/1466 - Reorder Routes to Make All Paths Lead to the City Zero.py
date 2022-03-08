class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:  # 
        seen = set([0])
        out = 0
        old = []
        while connections:
            start, finish = connections.pop()
            if finish in seen:
                seen.add(start)
            elif start in seen:
                seen.add(finish)
                out += 1
            else:
                old.append((start, finish))
            if not connections:
                connections = old
                old = []
        return out
