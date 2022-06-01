# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(
            self, head: Optional[ListNode],
            nums: List[int]) -> int:  # 28.38% 8.52%
        out = []
        set_nums = set(nums)
        seen = set()
        cur = set()
        while head.next:
            if head.val in set_nums and head.next.val in set_nums:
                cur.update([head.val, head.next.val])
                seen.update([head.val, head.next.val])
            else:
                if cur:
                    out.append(cur)
                cur = set()
            head = head.next
        if cur:
            out.append(cur)
        return len(out) + len(set_nums-seen)

    def numComponents_v2(
            self, head: Optional[ListNode],
            nums: List[int]) -> int:  # 70.96% 72.49%
        out = []
        set_nums = set(nums)
        cur = set()
        while head.next:
            if head.val in set_nums and head.next.val in set_nums:
                cur.update([head.val, head.next.val])
                set_nums.discard(head.val)
            else:
                if cur:
                    if head.val in set_nums:
                        cur.add(head.val)
                        set_nums.discard(head.val)
                    out.append(cur)
                cur = set()
            head = head.next
        if cur:
            out.append(cur)
            set_nums.discard(head.val)
        return len(out) + len(set_nums)

    def numComponents_best_speed(self, head, nums) -> int:
        nums = set(nums)
        cnt = 0
        while head:
            if head.val not in nums:
                head = head.next
            else:
                while head and head.val in nums:
                    head = head.next
                cnt += 1
        return cnt
