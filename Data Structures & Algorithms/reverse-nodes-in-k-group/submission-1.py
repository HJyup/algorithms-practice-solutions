# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        dummy = ListNode()
        dummy.next = head

        curr = dummy
        while curr.next:
            start = curr.next

            last = start
            for _ in range(1, k):
                last = last.next
                
                if not last:
                    return dummy.next

            last_nxt = last.next
            last.next = None

            curr.next = last_nxt
            curr_nxt = start

            while start:
                nxt = start.next
                start.next = curr.next

                curr.next = start
                start = nxt

            curr = curr_nxt

        return dummy.next
        