class Solution:
    def maximumRemovals(self, s, p, removable):  # 9.47% 97.73%
        def check(idx):
            cur = s.copy()
            for i in removable[:idx]:
                cur[i] = ''
            cur = ''.join(cur)
            i = 0
            for char in p:
                i = cur.find(char)
                if i == -1:
                    return False
                cur = cur[i+1:]
            return True

        s = list(s)
        ans = 0
        left, right = 0, len(removable)
        while left <= right:
            mid = left + (right-left)//2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
