class Solution:
    def kWeakestRows(
            self,
            mat: List[List[int]],
            k: int) -> List[int]:  # 39.39% 74.80 %
        s_map = {}
        for i in range(len(mat)):
            count = mat[i].count(1)
            if count not in s_map:
                s_map[count] = []
            s_map[count].append(i)
        weakest = sorted(s_map.keys(), reverse=True)
        out = []
        while k:
            weak = weakest.pop()
            if len(s_map[weak]) < k:
                out.extend([s_map[weak]])
                k -= len(s_map[weak])
            else:
                out.extend([s_map[weak][:k]])
                k = 0
        return [x for arr in out for x in arr]

    def kWeakestRows_study_plan_bin_search(self, mat, k):  # 99.77% 90.09%
        arr = []
        heapify(arr)
        for i in range(len(mat)):
            left, right = 0, len(mat[0])-1
            while left <= right:
                mid = left + (right-left)//2
                if mat[i][mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            if left != -1:
                heappush(arr, (left, i))
        return [x[1] for x in sorted(arr)[:k]]

    def kWeakestRows_best(self, mat: List[List[int]], k: int) -> List[int]:
        result = [(sum(row), i) for i, row in enumerate(mat)]
        result.sort()
        return [idx for val, idx in result[:k]]

    def kWeakestRows_best_speed(self, mat, k):
        history = {}
        result = []
        for i in range(len(mat)):
            history[i] = sum(mat[i])
        for i in sorted(history.items(), key=lambda h: (h[1])):
            result.append(i[0])
            if len(result) == k:
                break
        return result

    def kWeakestRows_2nd_best_speed(self, mat, k):
        summ = []
        pos = [i for i in range(len(mat))]
        for i in mat:
            summ.append(sum(i))
        zipped_lists = zip(summ, pos)
        sorted_pairs = sorted(zipped_lists)
        tuples = zip(*sorted_pairs)
        summ, pos = [list(tuple) for tuple in tuples]
        return pos[:k]
