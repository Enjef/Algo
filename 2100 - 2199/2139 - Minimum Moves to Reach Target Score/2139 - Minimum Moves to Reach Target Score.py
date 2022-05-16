class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:  # 36.05% 67.15%
        total = 0
        while target != 1:
            if not target % 2 and maxDoubles:
                target //= 2
                maxDoubles -= 1
            elif not target % 2 and not maxDoubles:
                total += target - 1
                break
            else:
                target -= 1
            total += 1
        return total

    def minMoves_best_speed(self, target: int, maxDoubles: int) -> int:
        jumps = 0
        while maxDoubles and target > 1:
            jumps += 1 + target % 2
            target //= 2
            maxDoubles -= 1
        return jumps + target - 1

    def minMoves_2nd_best_speed(self, target: int, maxDoubles: int) -> int:
        ans = 0
        while maxDoubles and target != 1:
            if target % 2 == 0:
                target = target//2
                ans += 1
            else:
                target = (target-1)//2
                ans += 2
            maxDoubles -= 1
        return ans + target - 1

    def minMoves_best_memory(self, target: int, maxDoubles: int) -> int:
        if target == 1:
            return 0
        if maxDoubles == 0:
            return target - 1    
        return 1 + (target % 2) + self.minMoves(target // 2, maxDoubles - 1)
