class Solution:
    def destCity(self, paths: List[List[str]]) -> str:  # 10.23% 76.14%
        map_c = {}
        cur = paths[0][0]
        for depart, arrive in paths:
            map_c[depart] = arrive
        for _ in map_c:
            if cur in map_c:
                cur = map_c[cur]
            else:
                return cur

    def destCity_set(self, paths: List[List[str]]) -> str:  # 17.43% 76.14%
        depart_set = set()
        arrive_set = set()
        for depart, arrive in paths:
            depart_set.add(depart)
            arrive_set.add(arrive)
        return list(arrive_set - depart_set)[0]
