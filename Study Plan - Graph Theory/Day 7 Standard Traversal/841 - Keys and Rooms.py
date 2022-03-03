class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]):  # 26.80% 23.55%
        def dfs(cur, seen):
            if cur in seen:
                return
            seen.add(cur)
            for num in rooms[cur]:
                dfs(num, seen)
            return
        
        n = len(rooms)
        all_rooms = set(range(n))
        visited = set()
        dfs(0, visited)
        return not(all_rooms - visited)


class Solution_v2:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(cur, seen):
            if cur in seen:
                return
            seen.add(cur)
            for num in rooms[cur]:
                dfs(num, seen)
            return
        
        n = len(rooms)
        visited = set()
        dfs(0, visited)
        return len(rooms) == len(visited)
