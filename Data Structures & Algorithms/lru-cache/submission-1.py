class Node:
    def __init__(self, key: int, val: int):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # Maps the key to the node
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # Remove node from doubly linked list
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # Insert node before right
    def insert(self, node):
        self.right.prev.next, node.prev = node, self.right.prev
        self.right.prev, node.next = node, self.right

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else: 
            return -1
        
    def put(self, key: int, value: int) -> None:
        # If the key's already in the cache then update it's value
        if key in self.cache:
            self.cache[key].val = value
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return

        # Add the new key-value pair to the map
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # If we are over capacity then evict the LRU key-value pair
        if len(self.cache) > self.cap:
            del self.cache[self.left.next.key]
            self.remove(self.left.next)
            
        



        
