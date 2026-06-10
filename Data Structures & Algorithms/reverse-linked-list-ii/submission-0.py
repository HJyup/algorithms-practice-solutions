# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # find the point of the left
        # reverse until counter exceeds right
        # =)
        dummy = ListNode(0)
        dummy.next = head

        l_node = dummy
        for _ in range(left - 1):
            l_node = l_node.next
        
        curr = l_node.next
        first = curr
        l_node.next = None

        count = left - 1
        while count != right:
            nxt = curr.next

            curr.next = l_node.next
            l_node.next = curr

            curr = nxt
            count += 1

        first.next = curr
        return dummy.next
