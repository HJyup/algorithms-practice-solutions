# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        dummy = ListNode(-1)
        curr = dummy

        # Have idx to prevent comparing between nodes when the same value
        for idx, ls in enumerate(lists) :
            if ls:
                heapq.heappush(h, (ls.val, idx, ls))
        
        while h:
            _, idx, node = heapq.heappop(h)

            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(h, (node.next.val, idx, node.next))

        return dummy.next

        