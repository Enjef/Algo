class Solution:
    def trimMean(self, arr: List[int]) -> float:  # 7.36% 7.63%
        arr.sort()
        arr = arr[int(len(arr)*0.05):-int(len(arr)*0.05)]
        return sum(arr)/len(arr)

    def trimMean_twenty(self, arr: List[int]) -> float:  # 5.49% 67.20%
        n = len(arr)/20
        while n:
            arr.pop(arr.index(min(arr)))
            arr.pop(arr.index(max(arr)))
            n -= 1
        return sum(arr)/len(arr)

    def trimMean_best_speed(self, arr: List[int]) -> float:  # 38.42% 35.07%
        arr.sort()
        delete_target = int(len(arr) / 100 * 5)
        sub_arr = arr[delete_target: len(arr) - delete_target]
        return sum(sub_arr) / len(sub_arr)
