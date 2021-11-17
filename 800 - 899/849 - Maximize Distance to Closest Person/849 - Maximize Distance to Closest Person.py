class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:  # 50.33% 76.27%
        cur = len(seats)
        for i in range(len(seats)):
            if not seats[i]:
                seats[i] = cur
            else:
                cur = 1
            cur += 1
        cur = len(seats)
        for i in range(len(seats)-1, -1, -1):
            seats[i] = min(seats[i], cur)
            if seats[i] == 1:
                cur = 1
            cur += 1
        return max(seats)-1

    def maxDistToClosest_best_speed(self, seats: List[int]) -> int:
        left_interval = 0
        left_idx = 0
        while seats[left_idx] == 0:
            left_interval += 1
            left_idx += 1

        right_interval = 0
        right_idx = len(seats)-1
        while seats[right_idx] == 0:
            right_interval += 1
            right_idx -= 1

        max_interval = 0
        temp_interval = 0
        for i in range(left_idx, right_idx+1):
            if seats[i] == 0:
                temp_interval += 1
            else:
                if max_interval < temp_interval:
                    max_interval = temp_interval
                temp_interval = 0
        max_interval = (max_interval+1)//2
        return max(left_interval, right_interval, max_interval)

    def maxDistToClosest_best_memoty(self, seats: List[int]) -> int:
        for i in range(len(seats)):
            if seats[i] == 1:
                break
        ans = i
        left = i
        right = i + 1
        while right < len(seats):
            if seats[right] == 1:
                ans = max(ans, (right-left)//2)
                left = right
                right += 1
            else:
                right += 1
        ans = max(ans, len(seats)-1-left)
        return ans
