class Solution:
    def shortestPathLength(self, graph: List[List[int]]): # 68.44% 58.92%
        n = len(graph)
        endMask = (1<<n) - 1
        vis = set()
        queue = [(node,1<<node,0) for node in range(n)]
        while queue:
            cur = queue.pop(0)
            if cur[1] == endMask:
                return cur[2]
            for neighbour in graph[cur[0]]:
                nextMask = (cur[1]|(1<<neighbour))
                if (neighbour, nextMask) not in vis:
                    vis.add((neighbour, nextMask))
                    queue.append((neighbour,nextMask,cur[2]+1))
