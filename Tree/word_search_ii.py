class TreeNode:
    def __init__(self) -> None:
        self.childlist = {}
        self.endofword = False

class Trie:
    def __init__(self) -> None:
        self.root = TreeNode()
    
    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.childlist:
                cur.childlist[c] = TreeNode()
            cur = cur.childlist[c]
        cur.endofword = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ## Be carefule, we CANNOT define the same name as class name in Python, like Trie = Trie()
        Tree = Trie()
        cur = Tree.root

        ## Build up the Trie with words
        for word in words:
            Tree.insert(word)
        
        row = len(board)
        column = len(board[0])
        visited = set()
        result = set()

        ## should put node(cur) as a parament passed into the inside function, since we will assign the cur to difference node
        ## it's not like list or dict, we can directly modify inside the function
        def dfsHelper(r, c, cur, word):
            if r < 0 or r >= row or c < 0 or c >= column or (r, c) in visited or board[r][c] not in cur.childlist:
                return 
            
            cur = cur.childlist[board[r][c]] ## should be put before if cur.endofword!!
            word += board[r][c]
            if cur.endofword:
                result.add(word)

            visited.add((r, c))
            dfsHelper(r+1, c, cur, word)
            dfsHelper(r-1, c, cur, word)
            dfsHelper(r, c+1, cur, word)
            dfsHelper(r, c-1, cur, word)
            visited.remove((r, c))
            return 
        
        for r in range(row):
            for c in range(column):
                dfsHelper(r, c, cur, "")
        
        return result