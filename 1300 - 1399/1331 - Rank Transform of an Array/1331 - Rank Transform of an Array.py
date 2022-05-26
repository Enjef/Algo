class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:  # 68.38% 58.82%
        arr_set = sorted(set(arr))
        loc = {el: idx for idx, el in enumerate(arr_set, 1)}
        for i, el in enumerate(arr):
            arr[i] = loc[el]
        return arr

    def arrayRankTransform_best_speed(self, arr: List[int]) -> List[int]:
        cp = sorted(set(arr))
        mp = {v: i+1 for i, v in enumerate(cp)}
        return [mp[n] for n in arr]

    def arrayRankTransform_best_memory(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        arr_sorted = sorted(arr)
        rank = 1
        ranks = {arr_sorted[0]: rank}
        for i in range(1, len(arr_sorted)):
            if arr_sorted[i] != arr_sorted[i-1]:
                rank += 1
                ranks[arr_sorted[i]] = rank
        result = []
        for num in arr:
            result.append(ranks[num])
        return result

    def arrayRankTransform_2nd_best_memory(self, arr: List[int]) -> List[int]:
        nums = {}
        for num in arr:
            nums[num] = nums.get(num, 0)
        counter = 1
        for num in sorted(nums):
            nums[num] = counter
            counter = counter + 1
        for index, num in enumerate(arr):
            arr[index] = nums[num]
        return arr
