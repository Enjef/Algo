class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):  # 9.91% 71.21%
        n = len(difficulty)
        new = sorted(zip(difficulty, profit))
        max_profit = [-1] * n
        for i in range(n):
            difficulty[i] = new[i][0]
            profit[i] = new[i][1]
            if i == 0:
                max_profit[i] = new[i][1]
            else:
                max_profit[i] = max(max_profit[i-1], new[i][1])
        result = 0
        for candidate in worker:
            left, right = 0, n - 1
            ans = -1
            while left <= right:
                mid = (left+right)//2
                if difficulty[mid] > candidate:
                    right = mid - 1
                else:
                    ans = mid
                    left = mid + 1
            if ans == -1:
                continue
            result += max_profit[ans]
        return result

    def maxProfitAssignment_best_speed(self, difficulty, profit, worker):
        jobs = sorted(zip(profit, difficulty))
        worker.sort()
        res = 0
        while worker and jobs:
            if jobs[-1][-1] > worker[-1]:
                jobs.pop()
            else:
                res += jobs[-1][0]
                worker.pop()
        return res

    def maxProfitAssignment_3d_best_speed(self, difficulty, profit, worker):
        n = len(profit)
        jobs = sorted([(difficulty[i], profit[i]) for i in range(n)])
        worker.sort()
        maxi = 0
        total = 0
        idx = 0
        for w in worker:
            while idx < n and w >= jobs[idx][0]:
                maxi = max(maxi, jobs[idx][1])
                idx += 1
            total += maxi
        return total

    def maxProfitAssignment_bin(self, difficulty, profit, worker):
        diff_pro = {}
        for i in range(len(difficulty)):
            key = difficulty[i]
            v = diff_pro.get(key)
            if v:
                diff_pro[key] = max(diff_pro[key], profit[i])
            else:
                diff_pro[key] = profit[i]
        sorted_diff = sorted(list(diff_pro.keys()))
        max_pros = [0]
        max_pro = 0
        for d in sorted_diff:
            max_pro = max(max_pro, diff_pro[d])
            max_pros.append(max_pro)
        res = 0
        for w in worker:
            idx = bisect_right(sorted_diff, w)
            res += max_pros[idx]
        return res

    def maxProfitAssignment_best_memory(self, difficulty, profit, worker):
        L = list(map(list, zip(difficulty, profit)))
        L.sort()
        n = len(L)
        for i in range(1, n):
            L[i][1] = max(L[i][1], L[i-1][1])
        res = 0
        for x in worker:
            j = bisect.bisect_right(L, [x, 10**6])-1
            if j > -1:
                res += L[j][1]
        return res
