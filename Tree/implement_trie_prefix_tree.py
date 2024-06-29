## remeber! every data structure, like linked list or tree, we should have a "class node" as well
class TreeNode:
    def __init__(self):
        self.childlist = {}
        self.endofword = False


class Trie:
    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.childlist:
                cur.childlist[c] = TreeNode()
            cur = cur.childlist[c]
        cur.endofword = True        

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.childlist:
                return False
            cur = cur.childlist[c]
        return cur.endofword

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.childlist:
                return False
            cur = cur.childlist[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)