# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 42.58% 75.71% (99.18% 75.71%)
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
        left = []
        right = []
        while head:
            if head.val < x:
                left.append(head)
            else:
                right.append(head)
            head = head.next
        left.extend(right)
        left[-1].next = None
        for i in range(len(left)-1):
            left[i].next = left[i+1]
        return left[0]

    def partition_best_speed(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode()
        dummy2 = ListNode()
        ptr1 = dummy1
        ptr2 = dummy2
        tmp = head
        while tmp:
            if tmp.val < x:
                ptr1.next = tmp
                ptr1 = ptr1.next
            else:
                ptr2.next = tmp
                ptr2 = ptr2.next
            tmp = tmp.next
        ptr2.next = None
        ptr1.next = dummy2.next
        return dummy1.next

    def partition_best_memory(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        sm = sm2 = ListNode(None)
        lr = lr2 = ListNode(None)
        temp = head
        while temp:
            if temp.val < x:
                sm.next = temp
                sm = temp
            else:
                lr.next = temp
                lr = temp
            temp = temp.next
        lr.next = None
        sm.next = lr2.next
        return sm2.next
