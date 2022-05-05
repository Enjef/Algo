class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:  # 32.75% 18.52%
        start = str(bin(start))[2:]
        goal = str(bin(goal))[2:]
        if len(goal) > len(start):
            start, goal = goal, start
        goal = goal.zfill(len(start))
        result = 0
        for i in range(len(start)):
            result += start[i] != goal[i]
        return result

    def minBitFlips(self, start: int, goal: int) -> int:  # 15.73% 18.52%
        start = bin(start)[2:]
        goal = bin(goal)[2:]
        if len(goal) > len(start):
            start, goal = goal, start
        goal = goal.zfill(len(start))
        result = 0
        for i in range(len(start)):
            result += start[i] != goal[i]
        return result

    def minBitFlips_best_speed(self, start: int, goal: int) -> int:
         return (start ^ goal).bit_count()

    def minBitFlips_2nd_best_speed(self, start: int, goal: int) -> int:
        ret = 0
        while start>0 or goal>0:
            ret +=  (start & 1)  ^ (goal & 1)
            start >>= 1
            goal >>= 1
        return ret

    def minBitFlips_best_memory(self, start: int, goal: int) -> int:
        a = bin(start)[2:]
        b = bin(goal)[2:]
        if len(a) > len(b):
            b = '0' * (len(a) - len(b)) + b
        else:
            a = '0' * (len(b) - len(a)) + a
        result = sum(1 for i, j in zip(a, b) if i != j)
        return result
