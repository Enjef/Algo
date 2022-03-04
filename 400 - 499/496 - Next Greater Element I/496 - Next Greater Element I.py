class Solution:
    def nextGreaterElement(self, nums1, nums2):  # 17.40% 97.75%
        ans = [-1]*len(nums1)
        for i, num1 in enumerate(nums1):
            for num2 in nums2[nums2.index(num1)+1:]:
                if num2 > num1:
                    ans[i] = num2
                    break
        return ans

    def nextGreaterElement_best_speed(self, nums1, nums2):
        stack = []
        d = {}
        for x in nums2:
            while stack and x > stack[-1]:
                d[stack.pop()] = x
            stack.append(x)
        res = []
        for x in nums1:
            res.append(d.get(x, -1))
        return res

    def nextGreaterElement_best_memory(self, nums1, nums2):
        index = {}
        ans = []
        for i in range(len(nums2)):
            index[nums2[i]] = i
        for i in range(len(nums1)):
            for j in range(index[nums1[i]]+1, len(nums2)):
                if nums2[j] > nums1[i]:
                    ans.append(nums2[j])
                    break
            else:
                ans.append(-1)
        return ans
