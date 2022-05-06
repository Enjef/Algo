# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head):  # 51.72% 48.35%
        if not head.next:
            return None
        prev = ListNode(next=head)
        slow = fast = head
        while fast and fast.next:
            prev = prev.next
            slow = slow.next
            fast = fast.next.next
        prev.next = prev.next.next
        return head

    def deleteMiddle_best_speed(
            self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        if head.next.next is None:
            head.next = None
            return head
        prev, curr, fast_ptr = head, head.next, head.next.next
        while fast_ptr and fast_ptr.next:
            prev = curr
            curr = curr.next
            fast_ptr = fast_ptr.next.next
        prev.next = curr.next
        return head

    def deleteMiddle_best_memory(self, head):
        if head is None:
            return head
        slow = head
        fast = slow.next
        if fast is None:
            return None
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return head
