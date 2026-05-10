"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy = {}

        # Create copies of each variable
        curr = head
        while curr:
            copy[curr] = Node(curr.val)
            curr = curr.next

        # Populate pointers
        curr = head
        while curr:
            copy[curr].random = copy[curr.random] if curr.random else None
            copy[curr].next = copy[curr.next] if curr.next else None
            curr = curr.next

        return copy[head] if head else None