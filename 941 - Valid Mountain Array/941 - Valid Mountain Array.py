class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        up = False
        down = False
        index_max = arr.index(max(arr))
        for i in range(1, len(arr)):
            if arr[i-1] == arr[i]:
                return False
            if arr[i-1] > arr[i] and i <= index_max:
                return False
            if arr[i-1] < arr[i] and i > index_max:
                return False
            if arr[i-1] > arr[i]:
                down = True
            if arr[i-1] < arr[i]:
                up = True
        return up and down

    def validMountainArray_best(self, arr: List[int]) -> bool:
        n = len(arr)-1
        beg = 0
        end = n
        if(len(arr) > 2):
            while(beg != n and arr[beg] < arr[beg+1]):
                beg = beg+1
            while(end != 0 and arr[end] < arr[end-1]):
                end = end-1
            return beg == end and beg != 0 and end != n
        else:
            return False
