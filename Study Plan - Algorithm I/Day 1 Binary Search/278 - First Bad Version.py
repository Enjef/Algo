

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):  # 11.40% 42.19%
        left = 1
        right = n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left

    def firstBadVersion_rec(self, n):  # 83.51% 90.53%
        def rec(left, right):
            if left > right:
                return left
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                return rec(left, mid - 1)
            else:
                return rec(mid + 1, right)
        return rec(0, n)
