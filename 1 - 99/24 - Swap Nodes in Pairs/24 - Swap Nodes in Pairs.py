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

    def swapPairs_ds2_day_12(
            self,
            head: Optional[ListNode]) -> Optional[ListNode]:  # 67.75% 17.37%
        if not head or not head.next:
            return head
        dummy = prev = ListNode(next=head.next)
        while head and head.next:
            next_prev = head
            next_first = head.next.next
            cur_second = head.next
            prev.next = cur_second
            cur_second.next = head
            head.next = next_first
            prev = next_prev
            head = next_first
        return dummy.next

    def swapPairs_best_speed(
            self,
            head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, cur = dummy, head
        while cur and cur.next:
            nxtPair = cur.next.next
            scd = cur.next
            cur.next = nxtPair
            scd.next = cur
            prev.next = scd
            prev = cur
            cur = nxtPair
        return dummy.next 

    def swapPairs_best_memory(
            self,
            head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(next = head)
        pre = res
        while pre.next and pre.next.next:
            cur, post = pre.next, pre.next.next            
            cur.next, post.next = post.next, cur
            pre.next = post
            pre = pre.next.next
        return res.next
