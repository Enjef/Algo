class Solution:
    def allPathsSourceTarget(
            self,
            graph: List[List[int]]) -> List[List[int]]:  # 53.88% 42.65%
        def helper(waypoint, path=[0], res=[]):
            for i in waypoint:
                if i == len(graph)-1:
                    res.append(path+[i])
                helper(graph[i], path+[i], res)
            return res
        return helper(graph[0])

    def allPathsSourceTarget_best_speed(
            self,
            graph: List[List[int]]) -> List[List[int]]:

        def count_paths(start, end, temp, graph):
            if start == end:
                temp += str(start)
            else:
                temp += str(start) + ','
            if start == end:
                results.append([temp])
                return None
            for i in graph[start]:
                count_paths(i, end, temp, graph)
        results = []
        count_paths(0, len(graph) - 1, '', graph)
        return results

    def allPathsSourceTarget_best_memory(self, graph):
        paths = []
        n = len(graph)
        seen = []
        stack = [[0]]
        while stack:
            path = stack.pop()
            node = path[-1]
            if path not in seen:
                seen.append(path)
            if node == n-1:
                paths.append(path)
            for v in graph[node]:
                new_path = path + [v]
                if not new_path in seen:
                    stack.append(new_path)
        return paths
