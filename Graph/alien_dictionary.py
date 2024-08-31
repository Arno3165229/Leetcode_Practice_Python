from typing import (
    List,
)

class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alien_order(self, words: List[str]) -> str:
        # Write your code here
        adjmap = {c: set() for w in words for c in w}

        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            minLength = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLength] == w2[:minLength]: ## edge case
                return ""
            for j in range(minLength):
                if w1[j] != w2[j]:
                    adjmap[w2[j]].add(w1[j]) ## w2[j] > w1[j]
                    break
        
        visited = set()
        cycle = set()
        output = []

        ##topological sort
        def dfs(c):
            if c in visited:
                return True
            if c in cycle:
                return False
            
            cycle.add(c)
            for adj in adjmap[c]:
                if not dfs(adj):
                    return False
            cycle.remove(c)
            visited.add(c)
            output.append(c)
            return True

        for c in adjmap:
            if not dfs(c):
                return ""
        
        return "".join(output)