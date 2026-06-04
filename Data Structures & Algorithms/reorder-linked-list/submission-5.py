# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle - 1, reverse, merge
        if not head.next:
            return None

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        first = head

        # reverse
        dummy = ListNode(-1)
        while second:
            val = second
            second = second.next
            val.next = dummy.next
            dummy.next = val

        second = dummy.next

        # merge into first
        while second:
            val = second
            second = second.next
            val.next = None
            val.next = first.next
            first.next = val
            first = first.next.next

        return None