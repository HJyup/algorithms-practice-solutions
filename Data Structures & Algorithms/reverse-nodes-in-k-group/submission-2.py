# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 1. iterate until get k (prev to first (dummy), end)
        # 2. save nxt from end
        # 3. start iterating towards end (important, safe first value after dummy)
        # 4. reverse
        # 5. connect next first to nxt from step 2
        # 6. start from node, which you saved at step 3
        if k == 1:
            return head

        def reversePart(start: ListNode, end: ListNode) -> ListNode:
            new_cycle = end.next
            new_end = start.next

            curr = new_end
            for _ in range(k):
                nxt = curr.next
                curr.next = start.next
                start.next = curr
                curr = nxt
                
            new_end.next = new_cycle
            return new_end


        dummy = ListNode(-1)
        dummy.next = head

        prev, curr = dummy, dummy
        count = 0
        while curr:
            if count == k:
                curr = reversePart(prev, curr)
                prev = curr
                count = 0
            else:
                curr = curr.next
                count += 1

        return dummy.next