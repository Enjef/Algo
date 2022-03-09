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
