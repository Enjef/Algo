class Solution:
    def canVisitAllRooms(
            self,
            rooms: List[List[int]]) -> bool:  # 21.25%-92.69%  98.92%
        visited = set()
        keys = rooms[0]
        visited.add(0)
        while keys:
            temp = []
            for key in keys:
                if key in visited:
                    continue
                visited.add(key)
                temp.extend(rooms[key])
            keys = temp
        return len(rooms) == len(visited)
