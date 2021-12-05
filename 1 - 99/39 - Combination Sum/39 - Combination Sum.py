class Solution:
    def combinationSum_mock(
            self,
            candidates: List[int],
            target: int) -> List[List[int]]:  # 5.01% 78.42%
        def generate(arr, cur, tar, out):
            if tar == 0:
                out.add(tuple(sorted(cur)))
                return out
            if tar < 0:
                return out
            for num in arr:
                generate(arr, cur+[num], tar-num, out)
            return out
        return generate(candidates, [], target, set())

    def combinationSum_best_speed(
            self,
            candidates: List[int],
            target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        def dfs(target, route, start):
            if target == 0:
                return route
            else:
                for i in range(start, len(candidates)):
                    candidate = candidates[i]
                    if target < candidate:
                        return False
                    else:
                        cur_path = dfs(
                            target - candidate, route + [candidate], i
                        )
                        if cur_path:
                            res.append(cur_path)
        dfs(target, [], 0)
        return res


    def combinationSum_best_memory(
            self,
            candidates: List[int],
            target: int) -> List[List[int]]:
        solutions=set()
        self.cs(sorted(candidates), target, [], solutions)
        return list(solutions)


    def cs(self, candidates, target, path, solutions):
        if target == 0:
            solutions.add(tuple(sorted(path)))
            return
        for candidate in candidates:
            if candidate>target:
                break
            path.append(candidate)
            self.cs(candidates, target-candidate, path, solutions)
            path.pop()
