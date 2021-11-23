class Solution:
    def rotateString(self, s: str, goal: str) -> bool:  # 58.37%  75.15%
        if len(s) != len(goal):
            return False
        for i in range(len(s)):
            if s[i:] + s[:i] == goal:
                return True
        return False

    def rotateString_best_speed(self, s: str, goal: str) -> bool:
        if len(s) == len(goal):
            new = goal + goal
            return s in new

    def rotateString_best_memory(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s + s
