from collections import deque
from heapq import heappush, heappop


class Solution:
    # 77.22% 46.07% (90.49% 38.85%)
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        res = []
        arr = []
        tasks = sorted([x+[i] for i, x in enumerate(tasks)], reverse=True)
        cur_time = 1
        while tasks:
            while tasks and tasks[-1][0] <= cur_time:
                heappush(arr, tasks.pop()[1:])
            if not arr:
                cur_time = tasks[-1][0]
                heappush(arr, tasks.pop()[1:])
                continue
            cur = heappop(arr)
            cur_time += cur[0]
            res.append(cur[1])
        while arr:
            res.append(heappop(arr)[1])
        return res


class Solution_best_speed:

    def load_queue(self, ready_queue, waiting_queue, current_time):
        while waiting_queue:
            (enqueue_time, process_time, idx) = waiting_queue[0]
            if (enqueue_time > current_time):
                return
            waiting_queue.popleft()
            heappush(ready_queue, (process_time, idx))

    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        if len(tasks) == 0:
            return []
        order = []
        tasks = [(*task, i) for i, task in enumerate(tasks)]
        tasks.sort()
        ready_queue = []
        waiting_queue = deque(tasks)
        current_time = 0
        while waiting_queue or ready_queue:
            if ready_queue:
                process_time, idx = heappop(ready_queue)
                current_time += process_time
                order.append(idx)
                self.load_queue(ready_queue, waiting_queue, current_time)
            else:
                current_time, _, _ = waiting_queue[0]
                self.load_queue(ready_queue, waiting_queue, current_time)
        return order


class Solution_3d_best_speed:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        unavailable = []
        for i, (enqtime, proctime) in enumerate(tasks):
            unavailable.append((enqtime, proctime, i))

        orderExecuted = []
        unavailable = collections.deque(sorted(unavailable))
        available = []
        time = 0
        while available or unavailable:
            while not available or (unavailable and unavailable[0][0] <= time):
                ptime, proctime, i = unavailable.popleft()
                time = max(time, ptime)
                heapq.heappush(available, (proctime, i))

            proctime, i = heapq.heappop(available)
            time += proctime
            orderExecuted.append(i)
        return orderExecuted


class Solution_best_memory:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        new = []
        index = 0
        max_time = 0
        for t in tasks:
            max_time = max(t[0], max_time)
            t.append(index)
            new.append(t)
            index += 1
        end = len(tasks)
        task = new
        heapq.heapify(tasks)
        res = []
        cur = []
        time = tasks[0][0]
        while len(res) != end:
            while time >= tasks[0][0]:
                t = heapq.heappop(tasks)
                process = t[1]
                index = t[2]
                heapq.heappush(cur, [process, index])
                if len(tasks) == 0:
                    temp = [float('inf'), 1, -1]
                    heapq.heappush(tasks, temp)
            if len(cur) > 0:
                task = heapq.heappop(cur)
                time = time + task[0]
                res.append(task[1])
            else:
                next_task = tasks[0][0]
                time = next_task
        return res


class Solution_2nd_best_memory:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i].append(i)
        heapq.heapify(tasks)
        queue = []
        res = []
        ctime = 0
        while tasks or queue:
            if len(queue) == 0:
                ele = heapq.heappop(tasks)
                heapq.heappush(queue, [ele[1], ele[2], ele[0]])
                while tasks:
                    if ele[0] == tasks[0][0]:
                        ele = heapq.heappop(tasks)
                        heapq.heappush(queue, [ele[1], ele[2], ele[0]])
                    else:
                        break
            ptime, index, stime = heapq.heappop(queue)
            ctime = max(ctime, stime)
            res.append(index)
            while tasks:
                if tasks[0][0] <= ctime+ptime:
                    ele = heapq.heappop(tasks)
                    heapq.heappush(queue, [ele[1], ele[2], ele[0]])
                else:
                    break
            ctime = ctime + ptime
        return res
