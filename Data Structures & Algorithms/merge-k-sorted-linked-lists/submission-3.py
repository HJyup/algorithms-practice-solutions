# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Let's try to think how we can expand this problem from what we already know
        # 1. We know how to merge 2 linked lists. therefore can we try to reduce to this idea?
        heap = []

        dummy = ListNode()
        curr = dummy
        
        # Populate heap
        for i, node in enumerate(lists):
            heapq.heappush(heap, (node.val, i, node))

        # Merge values
        while heap:
            _, i, node = heapq.heappop(heap)
            nxt = node.next

            if nxt:
                heapq.heappush(heap, (nxt.val, i, nxt))

            node.next = None
            curr.next = node
            curr = curr.next

        return dummy.next