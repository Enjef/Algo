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
                if not(-1 < cur < end) or cur in seen or cur in bad:
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

    def minimumJumps_best_speed(
            self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forb = set(forbidden)
        ans = 0
        q = [[0, 0]]
        visit = set()
        visit.add(0)
        if a > b:
            maxlimit = x+2*b
        else:
            maxlimit = max(x, max(forbidden))+2*b
        while (q):
            tmp = []
            for pos, flag in q:
                if pos == x:
                    return ans
                forw, back = pos+a, pos-b
                if (
                        back >= 0 and back not in forb and
                        back not in visit and back <= maxlimit and flag < 1):
                    tmp.append([back, flag+1])
                    visit.add(back)
                if (
                        forw >= 0 and forw not in forb and
                        forw not in visit and forw <= maxlimit):
                    tmp.append([forw, 0])
                    visit.add(forw)
            ans += 1
            q = tmp
        return -1

    def minimumJumps_best_memory(
            self, forbidden: List[int], a: int, b: int, x: int) -> int:
        q = [[0, 0]]
        k = 0
        seen = set()
        bound = max(max(forbidden)+a+b, x+b)
        while k < 5000:
            child = []
            while q:
                item = q .pop()
                curr, state = item
                if curr == x:
                    return k
                if curr in forbidden:
                    continue
                fwd = curr+a
                if fwd in forbidden or fwd < 0 or fwd > bound or fwd in seen:
                    pass
                else:
                    child.append([fwd, 0])
                    seen.add(fwd)
                if state == 0:
                    bwd = curr-b
                    if bwd in forbidden or bwd < 0 or bwd > bound or bwd in seen:
                        pass
                    else:
                        child.append([bwd, 1])
                        seen.add(fwd)
            if not child:
                return -1
            k += 1
            q = child
        return -1
