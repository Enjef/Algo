class Solution:
    # 93.81% 29.75% (51.38% 86.98%)
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        travel = [0] + travel
        n = len(travel)
        cur_m = cur_p = cur_g = 0
        last_m = last_p = last_g = -1
        for i in range(n):
            cur = garbage[i]
            cur_m += travel[i]
            cur_p += travel[i]
            cur_g += travel[i]
            if 'M' in cur:
                last_m = i
                cur_m += cur.count('M')
            if 'P' in cur:
                last_p = i
                cur_p += cur.count('P')
            if 'G' in cur:
                last_g = i
                cur_g += cur.count('G')
        if last_m == -1:
            cur_m = 0
        else:
            cur_m -= sum(travel[last_m+1:])
        if last_p == -1:
            cur_p = 0
        else:
            cur_p -= sum(travel[last_p+1:])
        if last_g == -1:
            cur_g = 0
        else:
            cur_g -= sum(travel[last_g+1:])
        return cur_m + cur_p + cur_g

    # 29.51% 86.98%
    def garbageCollection_v2(self, garbage: List[str], travel: List[int]) -> int:
        def helper(test):
            cur_m = 0
            last_m = -1
            for i in range(n):
                cur = garbage[i]
                cur_m += travel[i]
                if test in cur:
                    last_m = i
                    cur_m += cur.count(test)
            if last_m == -1:
                return 0
            return cur_m - sum(travel[last_m+1:])

        travel = [0] + travel
        n = len(travel)
        return helper('M') + helper('P') + helper('G')

    # 40.09% 86.98%
    def garbageCollection_v3(self, garbage: List[str], travel: List[int]) -> int:
        travel = [0] + travel
        n = len(travel)
        res = 0
        for test in 'MPG':
            cur_m = 0
            last_m = -1
            for i in range(n):
                cur = garbage[i]
                cur_m += travel[i]
                if test in cur:
                    last_m = i
                    cur_m += cur.count(test)
            if last_m != -1:
                res += cur_m - sum(travel[last_m+1:])
        return res


class Solution_best_speed:
    def garbageCollection_best_speed(self, garbage: List[str], travel: List[int]) -> int:
        last = dict()
        res = 0
        count = 0
        for i in range(len(garbage)-1, -1, -1):
            if count < 3:
                for c in garbage[i]:
                    if c not in last:
                        last[c] = i
                        count += 1
            res += len(garbage[i])
        s = 0
        j = 0
        for index in sorted(last.values()):
            while j < index:
                s += travel[j]
                j += 1
            res += s
        return res

    def garbageCollection_2nd_best_speed(self, garbage: List[str], travel: List[int]) -> int:
        glist = garbage[::-1]
        l = len(garbage)
        m = p = g = total = 0
        for i in range(len(glist)):
            if not m:
                if glist[i].find('M') is not -1:
                    m = l - 1 - i
            if not p:
                if glist[i].find('P') is not -1:
                    p = l - 1 - i
            if not g:
                if glist[i].find('G') is not -1:
                    g = l - 1 - i
            if p and g and m:
                break
        for s in garbage:
            total += len(s)
        if p:
            total += sum(travel[:p])
        if g:
            total += sum(travel[:g])
        if m:
            total += sum(travel[:m])
        return total


class Solution_best_memory:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        travel.insert(0, 0)

        def travel_find(garbage, obj, travel):
            curr_time = 0
            total_time = 0
            for i in range(len(garbage)):
                counter = 0
                if obj in garbage[i]:
                    counter = garbage[i].count(obj)
                    garbage[i] = garbage[i].replace(obj, '')
                    curr_time += counter + travel[i]
                    total_time = curr_time
                else:
                    curr_time += travel[i]
            return total_time
        count = 0
        for i in 'GPM':
            count += travel_find(garbage, i, travel)
        return count

    def garbageCollection_2nd_best_memory(self, garbage: List[str], travel: List[int]) -> int:
        g = m = p = False
        time = 0
        while len(travel):
            t = travel.pop()
            s = garbage.pop()
            if sum([g, m, p]) < 3:
                if 'G' in s:
                    g = True
                if 'M' in s:
                    m = True
                if 'P' in s:
                    p = True
            time += sum([g, m, p]) * t + len(s)
        time = time + len(garbage[0])
        return time
