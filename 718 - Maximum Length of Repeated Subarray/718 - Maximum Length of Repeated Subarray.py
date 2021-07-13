class Solution:
    def findLength(self, nums1, nums2):  # 5% 77.75%
        x_map = [[0] * (len(nums1)+1) for _ in range(len(nums2)+1)]
        out = 0
        for i in range(1, len(nums2)+1):
            for j in range(1, len(nums1)+1):
                if nums1[j-1] == nums2[i-1]:
                    x_map[i][j] = x_map[i-1][j-1] + 1
                out = max(out, x_map[i][j])
        return out

    def findLength_1(self, nums1, nums2):  # 29.65% 98.43%
        x_map = [[0] * (len(nums1)+1) for _ in range(2)]
        out = 0
        for i in range(1, len(nums2)+1):
            for j in range(1, len(nums1)+1):
                if nums1[j-1] == nums2[i-1]:
                    x_map[1][j] = x_map[0][j-1] + 1
                else:
                    x_map[1][j] = 0
                out = max(out, x_map[1][j])
            x_map[0] = x_map[1][:]
        return out

    def findLength_top_seven(self, nums1, nums2):  # 99.57% 90.68%
        out = 0
        nums1_str = ''.join([chr(x) for x in nums1])
        temp = ''
        for el in nums2:
            temp += chr(el)
            if temp in nums1_str:
                out = len(temp)
            else:
                temp = temp[1:]
        return out
