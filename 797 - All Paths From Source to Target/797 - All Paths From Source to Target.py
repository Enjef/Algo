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
