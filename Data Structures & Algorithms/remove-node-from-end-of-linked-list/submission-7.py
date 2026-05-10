# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # To make removal from the head easier, we will introduce the dummy node
        dummy = ListNode()

        # Connect dummy with a head
        dummy.next = head

        left = n
        fast = head

        while left > 0:
            fast = fast.next
            left -= 1

        slow = dummy
        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy.next