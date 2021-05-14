class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return nums
        out = []
        temp = ""
        for i in range(len(nums)-1):
            if abs(nums[i] - nums[i+1]) == 1:
                print("yeah")
                if temp:
                    temp = temp[:temp.index(">") + 1] + str(nums[i + 1])
                else:
                    temp += str(nums[i]) + "->" + str(nums[i + 1])
            elif temp:
                out.append(temp)
                temp = ""
            else:
                out.append(str(nums[i]))
        if temp:
            out.append(temp)
            return out
        out.append(str(nums[-1]))
        return out
