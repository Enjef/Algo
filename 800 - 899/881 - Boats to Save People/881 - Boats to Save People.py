class Solution:
    # 96.91% 18.19% (61.30% 60.46%)
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        result = len(people)
        people.sort()
        left, right = 0, result - 1
        while people[right] >= limit:
            right -= 1
        while left < right:
            cur = people[left] + people[right]
            if cur > limit:
                right -= 1
            else:
                result -= 1
                left += 1
                right -= 1
        return result
