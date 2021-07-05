class Solution:
    def findCenter_my(self, edges: List[List[int]]) -> int:  # 62.18%
        e_map = {}
        for edge in edges:
            for i in edge:
                if i not in e_map:
                    e_map[i] = 1
                else:
                    return i

    def findCenter_best(self, edges: List[List[int]]) -> int:
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]
        elif edges[0][1] == edges[1][0] or edges[0][1] == edges[1][1]:
            return edges[0][1]
