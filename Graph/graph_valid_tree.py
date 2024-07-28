from typing import (
    List,
)

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # write your code here
        if n == 0:
            return True
        
        hashmap = {i: [] for i in range(n)}
        for node1, node2 in edges:
            hashmap[node1].append(node2)
            hashmap[node2].append(node1)
        
        visited = set()

        def dfs(node, prev):
            if node in visited:
                return False
            
            visited.add(node)
            for neighbor in hashmap[node]:
                if neighbor != prev:
                    if not dfs(neighbor, node):
                        return False
            return True
        
        ## remember to check the length of visited. Tree is not allowed for two separate graph.
        return dfs(0, 0) and len(visited) == n