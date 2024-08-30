class Node:
    def __init__(self, key, val, prev, next):
        self.key = key
        self.value = val
        self.prev = prev
        self.next = next

## Remember, hashmap is unordered, so we need to use double linked list to keep the order.
class LRUCache:
    def __init__(self, capacity: int):
        self.k = capacity
        self.lru = {}
        self.left = Node(-1, 0, None, None)  ## self.left.next -> recent use 
        self.right = Node(-1, 0, None, None) ## self.right.prev -> least use
        self.left.next = self.right
        self.right.prev = self.left
    
    ## Maintain the linked list structure
    def insert(self, node):
        tmp = self.left.next
        tmp.prev = node
        node.next = tmp
        self.left.next = node
        node.prev = self.left

    ## Maintain the linked list structure
    def delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key in self.lru:
            self.delete(self.lru[key])
            self.insert(self.lru[key])
            return self.lru[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            self.delete(self.lru[key])
            del self.lru[key]
        self.lru[key] = Node(key, value, None, None)
        self.insert(self.lru[key])

        if len(self.lru) > self.k:
            lru_node = self.right.prev
            self.delete(lru_node)
            del self.lru[lru_node.key] ## remove the key in hashmap to maintain the size of hashmap, that's why the node need to store the key.

        return