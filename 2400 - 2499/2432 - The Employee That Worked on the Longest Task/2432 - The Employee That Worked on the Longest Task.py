class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        max_time = logs[0][1]
        emp_id = logs[0][0]
        for i in range(1, len(logs)):
            cur = logs[i][1] - logs[i-1][1]
            if cur > max_time:
                emp_id = logs[i][0]
            if cur == max_time:
                emp_id = min(emp_id, logs[i][0])
            max_time = max(max_time, cur)
        return emp_id

    def hardestWorker_best(self, n: int, logs: List[List[int]]) -> int:
        mx = (-1, -1)
        lst = 0
        for i in range(len(logs)):
            mx = max(mx, (logs[i][1] - lst, -logs[i][0]))
            lst = logs[i][1]
        return -mx[1]
