class Solution:
    # 22.26% 71.31%
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        coords = {num: i for i, num in enumerate(nums)}
        for old, new in operations:
            nums[coords[old]] = new
            coords[new] = coords[old]
        return nums

    def arrayChange_best_speed(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dic = {num: i for i, num in enumerate(nums)}
        for s, e in operations:
            i = dic[s]
            nums[i] = e
            dic[e] = i
            del dic[s]
        return nums

    def arrayChange_2nd_best_speed(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        index = {val: i for i, val in enumerate(nums)}
        for old, new in operations:
            x = index[old]
            nums[x] = new
            index[new] = x
        return nums

    def arrayChange_best_memory(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        hashmap = {}
        while operations:
            cad = operations.pop()
            if cad[1] in hashmap:
                hashmap[cad[0]] = hashmap[cad[1]]
            else:
                hashmap[cad[0]] = cad[1]
        for i in range(len(nums)):
            cad = nums[i]
            if cad in hashmap:
                nums[i] = hashmap[cad]
        return nums
