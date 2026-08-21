"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        # key is the old node and value is the new node
        oldToNew = {}
        
        def dfs(node):
            # if the copy already has been created then just return it
            if node in oldToNew:
                return oldToNew[node]
            
            # otherwise create a copy of the node and add the copy to 
            # our map
            copy = Node(node.val)
            oldToNew[node] = copy

            # append all the copies of the neighbors to our neighbor list
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))

            # propogate the newly copied node back to the caller
            return copy

        return dfs(node)