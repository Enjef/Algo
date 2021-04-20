# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    Your runtime beats 95.11 % of python3 submissions.
    Your memory usage beats 77.13 % of python3 submissions.
    '''
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        first = head.next
        second = head
        head = first
        second.next = first.next
        first.next = second
        prev = second
        if second.next:
            while prev.next.next:
                first = prev.next.next
                second = prev.next
                prev.next = first
                second.next = first.next
                first.next = second
                if second.next:
                    prev = second
                else:
                    break
        return head

    '''
    Your runtime beats 57.28 % of python3 submissions.
    Memory Usage: 14.3 MB, less than 16.40% of Python3 submissions.
    '''
    def swapPairs_2(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        prev = ListNode(next=head)
        head = head.next
        while prev.next.next:
            first = prev.next.next
            second = prev.next
            prev.next = first
            second.next = first.next
            first.next = second
            if second.next:
                prev = second
            else:
                break
        return head
