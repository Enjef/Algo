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

    def allPathsSourceTarget_v2(
            self,
            graph: List[List[int]]) -> List[List[int]]:  # 89.92% 76.13%
        def helper(level, cur=[0], out=[]):
            if level == n - 1:
                out.append(cur)
            for el in graph[level]:
                helper(el, cur+[el], out)
            return out
        n = len(graph)
        return helper(0)
