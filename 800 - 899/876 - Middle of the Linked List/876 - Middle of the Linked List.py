# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:  # 82.60% 43.81%
        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next
        count //= 2
        while count:
            count -= 1
            head = head.next
        return head

    def middleNode_best(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
