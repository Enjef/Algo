class Solution:
    def canChoose(self, groups, nums):  # 40.17% 52.99%
        x = 0
        for group in groups:
            for i in range(x, len(nums)):
                if nums[i] == group[0] and nums[i:i+len(group)]== group:
                    x = i + len(group)
                    break
            else:
                return False
        return True

    def exists_at(self, nums, index, group):
        for i in group:
            if nums[index] != i:
                return False
            index += 1
        return True

    def search(self, nums, num_index, group):
        while num_index <= len(nums) - len(group):
            if self.exists_at(nums, num_index, group):
                return num_index
            num_index += 1
        return -1

    def canChoose_best_speed(self, groups, nums):
        num_index = 0
        for group in groups:
            first_occurence = self.search(nums, num_index, group)
            if first_occurence == -1:
                return False
            num_index = first_occurence + len(group)
        return True

    def canChoose_2nd_best_memory(self, groups, nums):
        start, end = 0, len(nums)
        for group in groups:
            start = self.search_two(group,nums,start,end)
            if start == -1:
                return False
        return True
    
    def search_two(
            self, group, nums: List[int], start: int, end: int) -> int:
        i, j = start, 0
        while i < end and j < len(group):
            if nums[i] == group[j]:
                i += 1
                j += 1
                if j == len(group):
                    return i
            else:
                i = i-j+1
                j = 0
        return -1
