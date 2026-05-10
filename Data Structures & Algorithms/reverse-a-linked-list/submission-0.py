# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous, current = None, head
        # current: 1 -> 2 -> 3
        # previous : 3-> 2 -> 1 


        while current:
            temporary = current.next
            current.next = previous
            previous = current
            current = temporary
        return previous

        