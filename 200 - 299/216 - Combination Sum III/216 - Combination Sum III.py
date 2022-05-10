class Solution:
    def combinationSum3(
            self, k: int, n: int) -> List[List[int]]:  # 93.11% 79.39%
        def generate(num, cur_arr, target):
            if len(cur_arr) == k or target <= 0:
                if not target and len(cur_arr) == k:
                    out.add(tuple(cur_arr))
                return
            for el in range(num, 10):
                generate(el+1, cur_arr+[el], target-el)
            return

        out = set()
        generate(1, [], n)
        return out

    def combinationSum3_best_speed(self, k: int, n: int) -> List[List[int]]:
        def back_tracking(start, index, k, s, n, lst, res):
            if index == k:
                if s == n:
                    res.append(list(lst))
                return
            if s > n:
                return
            for j in range(start, 10):
                lst.append(j)
                back_tracking(j + 1, index + 1, k, s + j, n, lst, res)
                lst.pop()

        lst = []
        res = []
        back_tracking(1, 0, k, 0, n, lst, res)
        return res


class Solution_best_memory:
    def combinationSum3(self, k, n):
        res = []
        self.dfs(list(range(1, 10)), k, n, [], res)
        return res

    def dfs(self, nums, k, n, path, res):
        if k < 0 or n < 0:
            return
        if k == 0 and n == 0:
            res.append(path)
        for i in range(len(nums)):
            self.dfs(nums[i+1:], k-1, n-nums[i], path+[nums[i]], res)
