# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
            self,
            l1: Optional[ListNode],
            l2: Optional[ListNode]) -> Optional[ListNode]:  # 73.53% 45.64%
        num_one = 0
        num_two = 0
        out = ListNode()
        while l1:
            num_one = num_one * 10 + l1.val
            l1 = l1.next
        while l2:
            num_two = num_two * 10 + l2.val
            l2 = l2.next
        total = str(num_one + num_two)
        i = 0
        cur = out
        while i < len(total):
            cur.val = int(total[i])
            i += 1
            if i != len(total):
                cur.next = ListNode()
                cur = cur.next
        return out        
        
    def addTwoNumbers_best_speed(
            self,
            l1: Optional[ListNode],
            l2: Optional[ListNode]) -> Optional[ListNode]:
        sum1 = 0
        sum2 = 0
        while l1:
            sum1 = (sum1 * 10) + l1.val
            l1 = l1.next
        while l2:
            sum2 = (sum2 * 10) + l2.val
            l2 = l2.next
        total_sum = sum1 + sum2
        tail = None
        while total_sum > 0:
            tail = ListNode(val=total_sum%10, next=tail)
            total_sum //= 10
        return tail if tail else ListNode()

    def addTwoNumbers_best_memory(
            self,
            l1: Optional[ListNode],
            l2: Optional[ListNode]) -> Optional[ListNode]:
        v1 = v2 = ''
        while l1 or l2:
            if l1:
                v1 += str(l1.val)
                l1 = l1.next
            if l2:
                v2 += str(l2.val)
                l2 = l2.next
        total = str(int(v1) + int(v2))
        head = curr = ListNode(0)
        for i in range(len(total)):
            curr.next = ListNode(total[i])
            curr = curr.next
        return head.next
