class Solution:
    def slowestKey(
            self,
            releaseTimes: List[int],
            keysPressed: str) -> str:  # 8.37% 25.65%
        max_d = releaseTimes[0]
        out = [keysPressed[0]]
        for i in range(1, len(releaseTimes)):
            cur = releaseTimes[i] - releaseTimes[i-1]
            if cur > max_d:
                max_d = cur
                out = [keysPressed[i]]
            elif cur == max_d:
                out.append(keysPressed[i])
        out.sort()
        return out[-1]

    def slowestKey_refactored(
            self,
            releaseTimes: List[int],
            keysPressed: str) -> str:  # 8.37% 55.83%
        max_d = releaseTimes[0]
        out = 0
        for i in range(1, len(releaseTimes)):
            cur = releaseTimes[i] - releaseTimes[i-1]
            if cur > max_d:
                max_d = cur
                out = i
            elif cur == max_d:
                if keysPressed[out] < keysPressed[i]:
                    out = i
        return keysPressed[out]

    def slowestKey_best_speed(self, rel: List[int], key: str) -> str:  # ~7 ~80
        ind = 0  # 12.11% 5.25% with releaseTimes keysPressed variable names
        max_diff = rel[0]
        for i in range(1, len(rel)):
            diff = rel[i] - rel[i-1]
            if diff > max_diff:
                max_diff = diff
                ind = i
            elif diff == max_diff:
                if key[i] > key[ind]:
                    ind = i
        return key[ind]
