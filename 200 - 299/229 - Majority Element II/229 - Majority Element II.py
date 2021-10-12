class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:  # 18.75% 90.82%
        d = {}
        out = []
        for num in nums:
            d[num] = d.get(num, 0) + 1
        for el in d:
            if d[el] > len(nums) // 3:
                out.append(el)
        return out

    def majorityElement_second_to_best_speed(
            self,
            nums: List[int]) -> List[int]:
        t = set(nums)
        ans = list()
        for el in t:
            x = nums.count(el)
            if x > int(len(nums)/3):
                ans.append(el)
        return ans
