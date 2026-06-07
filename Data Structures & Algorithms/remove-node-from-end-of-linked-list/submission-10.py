# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # head == curr
        # we wanna find prev value

        fst = head
        for _ in range(n):
            fst = fst.next

        slow = head

        if not fst:
            return head.next
            
        while fst.next:
            fst = fst.next
            slow = slow.next        

        slow.next = slow.next.next
        return head