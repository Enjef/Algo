# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(
            self,
            head: Optional[ListNode]) -> Optional[ListNode]:  # 92.65% 59.04%
        first = prev = ListNode(next=head)
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                prev.next = head
            else:
                prev = prev.next
                head = head.next
        return first.next

    def deleteDuplicates_best_speed(
            self,
            head: Optional[ListNode]) -> Optional[ListNode]:
        fake = ListNode(0)
        fake.next = head
        pre = fake
        cur = head
        while cur:
            while cur and cur.next and cur.val == cur.next.val:
                cur = cur.next
            if(pre.next == cur):
                pre = pre.next
            else:
                pre.next = cur.next
            cur = cur.next
        return fake.next

    def deleteDuplicates_best_memory(
            self,
            head: Optional[ListNode]) -> Optional[ListNode]:
        nums = {}
        root = head
        while root != None:
            if root.val not in nums:
                nums[root.val] = 0
            nums[root.val] += 1
            root = root.next
        root = ListNode(0, None)
        current = root
        for i in nums.keys():
            if nums[i] == 1:
                current.next = ListNode(i, None)
                current = current.next
        return root.next
