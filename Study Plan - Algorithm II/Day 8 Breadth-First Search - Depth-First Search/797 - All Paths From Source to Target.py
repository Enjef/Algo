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
      