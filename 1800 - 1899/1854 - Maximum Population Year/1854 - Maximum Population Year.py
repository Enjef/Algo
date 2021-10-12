class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:  # 33.18% 65.67%
        log_map = {}
        for i in logs:
            for person in range(i[0], i[1]):
                if person not in log_map:
                    log_map[person] = 1
                else:
                    log_map[person] += 1
        max_val = max(log_map.values())
        out = [k for k, v in log_map.items() if v == max_val]
        return min(out)
