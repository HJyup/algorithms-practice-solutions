# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # The assumption
        # 1. Find the middle and prev before middle
        # 2. Remove connection between first and second half. 
        # 3. Make them as 2 different lists
        # 4. Reverse second half
        # 5. Merge lists
        if not head or not head.next:
            return

        # Find the middle
        slow, fast = head, head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Remove connection
        prev.next = None

        # Make them as 2 different lists
        first = head
        second = slow

        # Reverse second half
        prev = None
        curr = second

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        second = prev

        # Merge
        while first and second:
            f_next = first.next
            s_next = second.next

            first.next = second
            if not f_next:
                break

            second.next = f_next
            first = f_next
            second = s_next

        return None