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

    def majorityElement_best_speed(self, nums: List[int]) -> List[int]:
        l = []
        d = dict()
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        for n in d:
            if d[n] > int(len(nums)/3):
                l.append(n)
        return l

    def majorityElement_2nd_best_speed_new(self, nums: List[int]) -> List[int]:
        return [k for k,v in Counter(nums).items() if v >len(nums)//3 ]

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

    def majorityElement_mock(
            self,
            nums: List[int]) -> List[int]:  # 30.11% 0.00%
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        n = len(nums) // 3
        return [key for key, value in count.items() if value > n]
