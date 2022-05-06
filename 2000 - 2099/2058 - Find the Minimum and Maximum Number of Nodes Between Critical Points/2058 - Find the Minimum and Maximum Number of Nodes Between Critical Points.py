# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(
            self, head: Optional[ListNode]) -> List[int]:  # 24.51% 10.32%
        first = None
        min_dist = float('inf')
        prev_critical = None
        idx = 2
        prev = head
        head = head.next
        while head and head.next:
            if (
                    prev.val < head.val > head.next.val or
                    prev.val > head.val < head.next.val):
                if not first:
                    first = idx
                if prev_critical:
                    min_dist = min(min_dist, idx-prev_critical)
                prev_critical = idx
            idx += 1
            prev = head
            head = head.next
        return [-1, -1] if min_dist == float('inf') else [min_dist, prev_critical-first]

    def nodesBetweenCriticalPoints_3d_best_speed(
            self, head: Optional[ListNode]) -> List[int]:
        prev = head.val
        head = head.next
        if not head.next:
            return [-1, -1]
        first, last, currmin, curr = None, None, float("inf"), 1
        ahead = head.next
        while ahead:
            if prev > head.val < ahead.val or prev < head.val > ahead.val:
                if first is None: first = last = curr
                else:
                    currmin = min(currmin, curr - last)
                    last = curr
            prev, curr = head.val, curr + 1
            head, ahead = head.next, ahead.next
        return [currmin, last - first] if currmin != float("inf") else [-1, -1]

    def nodesBetweenCriticalPoints_best_memory(self, head):
        first = last = -1
        result = float('inf')
        i, prev, head = 0, head.val, head.next
        while head.next:
            if (
                max(prev, head.next.val) < head.val or
                min(prev, head.next.val) > head.val):
                    if first == -1:
                        first = i
                    if last != -1:
                        result = min(result, i-last)
                    last = i
            i += 1
            prev = head.val
            head = head.next
        return [result, last-first] if last != first else [-1, -1]
