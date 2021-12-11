class Solution:
    def relativeSortArray(
            self,
            arr1: List[int],
            arr2: List[int]) -> List[int]:  # 71.51% 66.87%
        out = []
        for num in arr2:
            while num in arr1:
                out.append(arr1.pop(arr1.index(num)))
        out += sorted(arr1)
        return out

    def relativeSortArray_sec_to_best(
            self,
            arr1: List[int],
            arr2: List[int]) -> List[int]:
        d = {}
        ans = []
        for n in arr1:
            d[n] = d.get(n, 0) + 1
        for n in arr2:
            ans += [n]*d[n]
            d[n] = 0
        for k, v in sorted(d.items()):
            ans += [k]*v
        return ans

class Solution:
    def relativeSortArray_mock(
            self,
            arr1: List[int],
            arr2: List[int]) -> List[int]:  # 39.45% 89.55%
        count = {}
        last = []
        first = []
        set_arr2 =set(arr2)
        for num in arr1:
            if num in set_arr2:
                count[num] = count.get(num, 0) + 1
            else:
                last.append(num)
        for num in arr2:
            first.extend([num]*count[num])
        last.sort()
        arr1[:] = first + last
        return arr1
