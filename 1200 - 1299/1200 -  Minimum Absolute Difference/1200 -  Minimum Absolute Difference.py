class Solution:
    def minimumAbsDifference(
            self,
            arr: List[int]) -> List[List[int]]:  # 28.86% 85.24%
        out = []
        arr.sort()
        min_diff = float('inf')
        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                diff = abs(arr[j] - arr[i])
                if diff < min_diff:
                    min_diff = diff
                    out.clear()
                    out.append([arr[i], arr[j]])
                elif diff == min_diff:
                    out.append([arr[i], arr[j]])
                else:
                    break
        return out

    def minimumAbsDifference_one_loop(
            self,
            arr: List[int]) -> List[List[int]]:  # 95.84% 85.24%
        out = []
        arr.sort()
        min_diff = float('inf')
        prev = arr[0]
        for i in range(1, len(arr)):
            cur = arr[i]
            diff = abs(cur - prev)
            if diff < min_diff:
                min_diff = diff
                out.clear()
                out.append([prev, cur])
            elif diff == min_diff:
                out.append([prev, cur])
            prev = cur
        return out

    def minimumAbsDifference_mock(
            self, arr: List[int]) -> List[List[int]]:  # 89.34% 99.70%
        diff = float('inf')
        out = set()
        arr.sort()
        for i in range(1, len(arr)):
            cur = abs(arr[i] - arr[i-1])
            if cur < diff:
                diff = cur
                out.clear()
                out.add((arr[i-1], arr[i]))
            elif cur == diff:
                out.add((arr[i-1], arr[i]))
        return sorted(out)
