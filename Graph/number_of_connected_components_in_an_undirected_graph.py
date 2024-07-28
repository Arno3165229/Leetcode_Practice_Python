## Solution1 DFS
from typing import (
    List,
)

class Solution:
    """
    @param n: the number of vertices
    @param edges: the edges of undirected graph
    @return: the number of connected components
    """
    def count_components(self, n: int, edges: List[List[int]]) -> int:
        hashmap = {i:[] for i in range(n)}

        for node1, node2 in edges:
            hashmap[node1].append(node2)
            hashmap[node2].append(node1)

        visited = set()

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            for neighbor in hashmap[node]:
                dfs(neighbor)
        
        res = 0

        for node in range(n):
            if node not in visited:
                dfs(node)
                res += 1
        
        return res


## Solution2 UnionFind
from typing import (
    List,
)

class Solution:
    """
    @param n: the number of vertices
    @param edges: the edges of undirected graph
    @return: the number of connected components
    """
    def count_components(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]] 
                node = parent[node]
            return node

        def union(node1, node2):
            parent1 = find(node1)
            parent2 = find(node2)

            if parent1 == parent2:
                return 0 
            
            if rank[parent2] > rank[parent1]:
                parent[parent1] = parent[parent2]
                rank[parent2] += rank[parent1]
            else:
                parent[parent2] = parent[parent1]
                rank[parent1] += rank[parent2]
            return -1
        
        result = n
        for node1, node2 in edges:
            result += union(node1, node2)
        
        return result
