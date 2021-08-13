class Solution:
    def minOperations(self, logs: List[str]) -> int:  # 53.76% 81.59%
        level = 0
        for action in logs:
            if action == './':
                continue
            if action == '../':
                if level > 0:
                    level -= 1
            else:
                level += 1
        return level

    def minOperations_best(self, logs: List[str]) -> int:
        depth = 0
        for log in logs:
            if log == '../':
                depth = max(0, depth - 1)
            elif log != './':
                depth += 1
        return depth
