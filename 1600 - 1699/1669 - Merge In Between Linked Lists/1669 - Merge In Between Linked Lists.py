# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1, a: int, b: int): # 36.49% 8.28%
        cur = list1
        while a > 1:
            cur = cur.next
            a -= 1
            b -= 1
        b_start = cur
        while b:
            cur = cur.next
            b -= 1
        b_start.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = cur.next
        return list1

    def mergeInBetween_best_speed(self, list1, a, b, list2):
        p = list1
        for _ in range(a - 1):
            p = p.next
        q = p.next
        for _ in range(b - a + 1):
            q = q.next
        p.next = list2
        while p.next:
            p = p.next
        p.next = q
        return list1

    def mergeInBetween_best_memory(self, list1, a, b, list2):
        prev=dummy=ListNode(0,list1)
        count=0
        while list1:
            if count==a:
                break
            count+=1
            prev=list1
            list1=list1.next
        prev.next=list2
        while list1:
            if count==b:
                break
            count+=1
            list1=list1.next
        while list2.next:
            list2=list2.next
        list2.next=list1.next
        return dummy.next
