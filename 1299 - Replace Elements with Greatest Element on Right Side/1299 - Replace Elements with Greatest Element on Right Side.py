class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:  # 34.35% 65.49%
        for i in range(len(arr)-1):
            arr[i] = max(arr[i+1:])
        arr[-1] = -1
        return arr

    def replaceElements_best(self, arr: List[int]) -> List[int]:
        currGreatest = -1
        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]
            arr[i] = currGreatest
            if temp > currGreatest:
                currGreatest = temp
        return arr

    def replaceElements_one(self, arr: List[int]) -> List[int]:  # 81% 99% 
        x_max = -1
        for i in range(len(arr)-1, -1, -1):
            arr[i], x_max = x_max, max(arr[i], x_max)
        return arr
