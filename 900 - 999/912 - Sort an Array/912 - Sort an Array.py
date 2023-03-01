class Solution:
    # 18.87% 89.03%
    def sortArray(self, nums: List[int]) -> List[int]:
        def heapify(arr, idx, n):
            cur_max = idx
            left, right = idx * 2 + 1, idx * 2 + 2
            if left < n and arr[left] > arr[cur_max]:
                cur_max = left
            if right < n and arr[right] > arr[cur_max]:
                cur_max = right
            if cur_max != idx:
                arr[cur_max], arr[idx] = arr[idx], arr[cur_max]
                heapify(arr, cur_max, n)

        N = len(nums)
        for i in range(N//2-1, -1, -1):
            heapify(nums, i, N)
        for i in range(N-1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            heapify(nums, 0, i)
        return nums


class Solution_best_memory:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(arr):
            if len(arr) > 1:
                mid = int(len(arr)//2)
                l1 = arr[:mid]
                l2 = arr[mid:]
                mergeSort(l1)
                mergeSort(l2)
                left = right = k = 0
                while left < len(l1) and right < len(l2):
                    if l1[left] <= l2[right]:
                        arr[k] = l1[left]
                        left += 1
                    else:
                        arr[k] = l2[right]
                        right += 1
                    k += 1

                while left < len(l1):
                    arr[k] = l1[left]
                    left += 1
                    k += 1
                while right < len(l2):
                    arr[k] = l2[right]
                    right += 1
                    k += 1
        mergeSort(nums)
        return nums
