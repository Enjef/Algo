# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:  # 7.42% 50.67%
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        n = len(arr)
        return max(x+y for x,y in zip(arr[:n//2], arr[n//2:][::-1]))

    def pairSum_best_speed(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        prev = None
        while fast:
            slow.next, prev, slow, fast = prev, slow, slow.next, fast.next.next
        res = 0
        while slow:
            v = prev.val + slow.val
            if res<v:
                res = v
            prev = prev.next
            slow = slow.next
        return res

    def pairSum_2nd_best_speed(self, head: Optional[ListNode]) -> int:
        ans = float("-inf")
        temp = slow = fast = head
        prev = None
        while fast and fast.next:
            fast, a, slow.next = fast.next.next, slow.next, prev
            prev, slow = slow, a
        while prev and slow:
            ans = max(ans, prev.val+slow.val)
            prev, slow = prev.next, slow.next
        return ans
