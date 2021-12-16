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

    def canVisitAllRooms_best_speed(self, rooms: List[List[int]]) -> bool:
        a = [False]*len(rooms)
        a[0] = True
        stack = [0]
        while stack:
            node = stack.pop()
            for i in rooms[node]:
                if not a[i]:
                    a[i] = True
                    stack.append(i)
        return all(a)

    def canVisitAllRooms_2nd_best_speed(self, rooms: List[List[int]]) -> bool:
        keys = set()
        self.dfs(0, rooms, keys)
        return len(keys) == len(rooms)
            
    def dfs(self, curr_room, rooms, keys):
        keys.add(curr_room)
        for ngh in rooms[curr_room]:
            if ngh not in keys:
                self.dfs(ngh, rooms, keys)

    def canVisitAllRooms_best_memory(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        visited[0] = True
        stack = [0]
        while stack:
            x = stack.pop()
            for keys in rooms[x]:
                if not visited[keys]:
                    visited[keys] = True
                    stack.append(keys)
        return all(visited)
