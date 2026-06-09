# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def merge(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            dummy = ListNode(-1)

            curr = dummy
            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next

                curr = curr.next

            curr.next = l1 or l2
            return dummy.next

        def mergeSort(left: int, right: int) -> Optional[ListNode]:
            if left == right:
                return lists[left]

            mid = (left + right) // 2
            low = mergeSort(left, mid)
            high = mergeSort(mid + 1, right)

            return merge(low, high)

        return mergeSort(0, len(lists) - 1)

            