
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node or node == None: return None
        visited = {}

        def dfs(node):
            if node.val not in visited:
                cloned_node = Node(val = node.val)
                visited[node.val] = cloned_node
            else: return visited[node.val]
            for neighbor in node.neighbors:
                visited[node.val].neighbors.append(dfs(neighbor))
            return cloned_node
        
        new__cloned_node = dfs(node)
        return new__cloned_node