class Solution:
    def minimumJumps(
            self, forbidden: List[int], a: int,
            b: int, x: int) -> int:  # 87.47% 53.07%
        bad = set(forbidden)
        end = 6000
        stack = [(0, True)]
        out = 0
        seen = set()
        while stack:
            next_jump = []
            for cur, prevm in stack:
                if not(-1<cur<end) or cur in seen or cur in bad:
                    continue
                seen.add(cur)
                if cur == x:
                    return out
                if prevm:
                    next_jump.append((cur+a, False))
                else:
                    next_jump.extend([(cur-b, True), (cur+a, False)])
            stack = next_jump
            out += 1
        return -1
