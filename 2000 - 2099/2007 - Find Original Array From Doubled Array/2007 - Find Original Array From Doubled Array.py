class Solution:
    # 21.53% 17.13%
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        counter = Counter(changed)
        original = set()
        out = []
        if 0 in counter:
            if counter[0] % 2:
                return []
            out += [0] * (counter[0]//2)
            del counter[0]
        for el in sorted(counter):
            if not counter[el]:
                continue
            elif el*2 not in counter or counter[el] > counter[el*2]:
                return []
            else:
                out.extend([el]*counter[el])
                original.add(el)
                counter[2*el] -= counter[el]
                counter[el] = 0
        return out if not any(counter.values()) else []

    # 33.24% 9.37%
    def findOriginalArray_v2(self, changed: List[int]) -> List[int]:
        counter = Counter(changed)
        original = set()
        out = []
        if 0 in counter:
            if counter[0] % 2:
                return []
            out += [0] * (counter[0]//2)
            del counter[0]
        for el in sorted(counter):
            if not counter[el]:
                continue
            elif el*2 not in counter or counter[el] > counter[el*2]:
                return []
            else:
                out.extend([el]*counter[el])
                original.add(el)
                counter[2*el] -= counter[el]
                counter[el] = 0
        return out

    def findOriginalArray_best_speed(self, changed: List[int]) -> List[int]:
        counter = collections.Counter(changed)
        res = []
        for k in counter.keys():
            if k == 0:
                if counter[k] % 2 > 0:
                    return []
                res += [0] * (counter[k] // 2)
            elif counter[k] > 0:
                x = k
                while x % 2 == 0 and x // 2 in counter:
                    x = x // 2
                while x in counter:
                    if counter[x] > 0:
                        res += [x] * counter[x]
                        if counter[x+x] < counter[x]:
                            return []
                        counter[x+x] -= counter[x]
                        counter[x] = 0
                    x += x
        return res

    def findOriginalArray_2nd_best_speed(self, changed: List[int]) -> List[int]:
        counter = Counter(changed)
        for n in sorted(counter):
            if n == 0 and counter[0] % 2 == 1:
                return []
            if counter[n] > counter[n*2]:
                return []
            if n:
                counter[n*2] -= counter[n]
            else:
                counter[n] //= 2
        return list(counter.elements())

    def findOriginalArray_3d_best_speed(self, changed: List[int]) -> List[int]:
        cnt = Counter(changed)
        sorted_keys = sorted(cnt.keys())
        res = []
        for k in sorted_keys:
            if cnt[k] == 0:
                continue
            while cnt[k]:
                cnt[k] -= 1
                if cnt[k * 2] == 0:
                    return []
                cnt[k * 2] -= 1
                res.append(k)
        return res

    def findOriginalArray_best_memory(self, changed: List[int]) -> List[int]:
        changed.sort()
        ret_val = []
        r = 1
        for a in range(len(changed)-1):
            l = a
            if r <= l:
                r = a+1
            val = True
            if changed[a] == -1:
                continue
            while val and r < len(changed):
                if changed[r] == -1:
                    r += 1
                elif 2*changed[l] == changed[r]:
                    ret_val.append(changed[l])
                    changed[l] = changed[r] = -1
                    r += 1
                elif 2 * changed[l] > changed[r]:
                    r += 1
                else:
                    val = False
        if len(ret_val) != len(changed)/2:
            return []
        return ret_val

    def findOriginalArray_2nd_best_memory(self, changed: List[int]) -> List[int]:
        n = len(changed)
        num_odd = sum([x % 2 for x in changed])
        if (n % 2 == 1) or (n - 2*num_odd < 0) or ((n - 2*num_odd) % 2 == 1):
            return []
        changed = sorted(changed)
        res = []
        while len(changed) > 0:
            x = changed.pop(0)
            res.append(x)
            i = bisect_left(changed, 2*x)
            if i >= len(changed) or changed[i] != 2*x:
                return []
            changed.pop(i)
        return res
