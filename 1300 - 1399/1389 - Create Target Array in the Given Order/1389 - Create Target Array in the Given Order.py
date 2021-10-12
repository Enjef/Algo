class Solution(object):
    def createTargetArray(self, nums, index):
        out = []
        for i in range(len(index)):
            out.insert(index[i], nums[i])
        return out
