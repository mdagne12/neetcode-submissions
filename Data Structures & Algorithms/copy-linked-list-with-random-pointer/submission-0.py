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

        # Create a hashmap that maps each node to it's deep copy
        curr = head
        hashmap = {None:None}
        while curr != None:
            hashmap[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr != None:
            # Set curr's deep copies pointer to the 
            # copies of what it points to
            hashmap[curr].next = hashmap[curr.next]
            hashmap[curr].random = hashmap[curr.random]
            curr = curr.next

        return hashmap[head]
