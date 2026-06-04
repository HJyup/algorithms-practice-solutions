# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:    
        # safe-guard
        if not head.next:
            return None

        # find the middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next # indicates the second half
        slow.next = None # remove connection for first half

        # reverse
        dummy = ListNode(-1)
        while second:
            val = second
            second = second.next
            val.next = dummy.next
            dummy.next = val

        rev = dummy.next
        first = head

        # merge into first
        while rev:
            val = rev
            rev = rev.next
            val.next = first.next
            first.next = val
            first = first.next.next

        return None