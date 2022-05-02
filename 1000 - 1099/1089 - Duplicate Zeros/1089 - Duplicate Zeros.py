class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:  # 65.91% 99.71%
        """
        Do not return anything, modify arr in-place instead.
        """
        new = []
        for el in arr:
            if el == 0:
                if len(new) + 1 == len(arr):
                    new.append(0)
                    break
                new.extend([0, 0])
            else:
                new.append(el)
            if len(new) >= len(arr):
                break
        arr[:] = new
        return

    def duplicateZeros_best_speed(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        n = len(arr)
        while(i<n):
            if arr[i] == 0:
                arr.insert(i,0)
                i += 1
                arr.pop()
            i += 1
