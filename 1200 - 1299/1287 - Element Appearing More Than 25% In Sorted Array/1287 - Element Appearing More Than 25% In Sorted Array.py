class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:  # 5.36% 7.72%
        for num in set(arr):
            if arr.count(num) > len(arr) // 4:
                return num
        return arr[0]

    def findSpecialInteger_dict_max(
            self,
            arr: List[int]) -> int:  # 32.25% # 16.69%
        n_map = {}
        for num in arr:
            n_map[num] = n_map.get(num, 0) + 1
        return max(n_map, key=n_map.get)

    def findSpecialInteger_count(self, arr: List[int]) -> int:  # 73.85% 37.98%
        if len(arr) < 4:
            return arr[len(arr)//2]
        out = [0, 0]
        cur = [0, 0]
        for num in arr:
            if num != cur[0]:
                if cur[1] > out[1]:
                    out = cur
                cur = [num, 0]
            else:
                cur[1] += 1
        if cur[1] > out[1]:
            out = cur
        return out[0]

    def findSpecialInteger_return_at_target(
            self,
            arr: List[int]) -> int:  # 99.88%  51.81%
        if len(arr) < 4:
            return arr[len(arr)//2]
        out = [0, 0]
        cur = [0, 0]
        for num in arr:
            if num != cur[0]:
                if cur[1] > out[1]:
                    out = cur
                cur = [num, 0]
            else:
                cur[1] += 1
                if cur[1] > len(arr) // 4:
                    return cur[0]
        if cur[1] > out[1]:
            out = cur
        return out[0]
