class Solution:
    def intersect_first(self, nums1, nums2):  # 87.40% 13.78%
        num_map = {}
        nums1.sort()
        nums2.sort()
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j] and nums1[i] not in num_map:
                num_map[nums1[i]] = 1
                i += 1
                j += 1
                continue
            if nums1[i] == nums2[j] and nums1[i] in num_map:
                num_map[nums1[i]] += 1
                i += 1
                j += 1
                continue
            if nums1[i] in num_map and nums2[j] not in num_map:
                i += 1
                continue
            if nums1[i] not in num_map and nums2[j] in num_map:
                j += 1
                continue
            if nums1[i] <= nums2[j]:
                i += 1
                continue
            if nums1[i] > nums2[j]:
                j += 1
                continue
        out = []
        print(num_map)
        for key in num_map:
            for _ in range(num_map[key]):
                out.append(key)
        return out

    def intersect_second(self, nums1, nums2):  # 20.88% 88.15%
        out = []
        nums1.sort()
        nums2.sort()
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                out.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] <= nums2[j]:
                i += 1
            else:
                j += 1
        return out

    def intersect_study_plan_version(
            self,
            nums1: List[int],
            nums2: List[int]) -> List[int]:  # 8.17% 90.08%
        nums1_map = {}
        nums2_map = {}
        for num in nums1:
            nums1_map[num] = nums1_map.get(num, 0) + 1
        for num in nums2:
            nums2_map[num] = nums2_map.get(num, 0) + 1
        for num in nums1_map:
            nums1_map[num] = min(nums1_map.get(num, 0), nums2_map.get(num, 0))
        out = []
        for el in nums1_map:
            if nums1_map[el]:
                out.extend([el] * nums1_map[el])
        return out

    def intersect_heap(self, nums1, nums2):  # 92.31% 88.15%
        heapify(nums1)
        heapify(nums2)
        res = []
        while nums1 and nums2:
            first, second = heappop(nums1),  heappop(nums2)
            if first == second:
                res.append(first)
            if first < second:
                heappush(nums2, second)
            elif second < first:
                heappush(nums1, first)
        return res

    def intersect_study_plan_bin_search(self, nums1, nums2):  # 59.33% 88.15%
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        nums2.sort()
        res = []
        for num in nums1:
            left, right = 0, len(nums2)-1
            while left <= right:
                mid = left + (right-left)//2
                if nums2[mid] == num:
                    res.append(num)
                    nums2.pop(mid)
                    break
                if nums2[mid] < num:
                    left = mid + 1
                else:
                    right = mid - 1
        return res

    def intersect_best_speed(self, nums1, nums2):
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        c3 = c1 & c2
        return list(c3.elements())

    def intersect_2nd_best_speed(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        nSet = Counter(nums1)
        res = []
        for i in nums2:
            if nSet[i]:
                res.append(i)
                nSet[i] -= 1
        return res
