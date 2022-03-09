class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:  # 66.56% 85.89%
        stack = [start]
        n = len(arr)
        seen = set()
        while stack:
            next_jump = []
            for jump in stack:
                if not(-1<jump<n) or jump in seen:
                    continue
                if not arr[jump]:
                    return True
                seen.add(jump)
                next_jump.extend([jump+arr[jump], jump-arr[jump]])
            stack = next_jump
        return False

    def canReach_best_speed(self, arr: List[int], start: int) -> bool:
        visited = set()
        n = len(arr)
        
        def find(i=start) :
            if arr[i] == 0 :
                return True
            if i in visited :
                return False
            visited.add(i)
            i_n = i + arr[i]
            if i_n < n and find(i_n) :
                return True
            i_n = i - arr[i]
            if i_n >= 0 and find(i_n) :
                return True
        return find()

    def canReach_memory_best(self, arr: List[int], start: int) -> bool:
        q = deque([start])
        visited = set()
        while q:
            cur_index = q.pop()
            if cur_index in visited:
                continue
            if arr[cur_index] == 0:
                return True
            adj_idx1 = cur_index + arr[cur_index] 
            adj_idx2 = cur_index - arr[cur_index] 
            if 0 <= adj_idx1 < len(arr) and adj_idx1 not in visited:
                q.appendleft(adj_idx1)
            if 0 <= adj_idx2 < len(arr) and adj_idx2 not in visited:
                q.appendleft(adj_idx2)
            visited.add(cur_index)
        return False
