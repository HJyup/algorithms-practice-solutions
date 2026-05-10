# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        queue = deque(lists)

        def merge(l1: ListNode, l2: ListNode):
            dummy = ListNode(-1)

            curr = dummy
            while l1 and l2:
                l1_val = l1.val
                l2_val = l2.val

                if l1_val < l2_val:
                    curr.next = l1
                    l1 = l1.next

                else:
                    curr.next = l2
                    l2 = l2.next

                curr = curr.next

            if l1:
                curr.next = l1

            if l2:
                curr.next = l2

            return dummy.next

        while len(queue) > 1:
            l1 = queue.popleft()
            l2 = queue.popleft()
            
            merged = merge(l1, l2)
            queue.append(merged)

        return queue[0]